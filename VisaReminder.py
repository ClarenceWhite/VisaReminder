from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from read_config import Config
from send_msg import Wechat


class VisaReminder:
    def RunReminder():
        #create a Config class object
        read_config = Config()
        #create a Wechat class object
        send_msg = Wechat()

        #get chrome driver path
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        #get requested link
        link = read_config.load()['link']
        driver.get(link)

        try:
            # find the first 'Next ' button and click on it
            element = WebDriverWait(driver, 7).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Next"))
            )
            first_next_element = driver.find_element(by=By.LINK_TEXT, value="Next")
            first_next_element.click()
        except:
            print("Error in first step => open page and click on the first next")

        try:
            # find the second 'Next ' button on the second page and click on it
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Next"))
            )
            second_next_element = driver.find_element(By.LINK_TEXT, "Next")
            second_next_element.click()
        except:
            print("Error in second step => click on the second next")

        try:
            #check if there are slots available
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"wizardForm-p-2\"]/div[4]/div/div/ul/li"))
            )
            time.sleep(5)
            check_alert = driver.find_element(By.XPATH, "/html/body/div/div/section/div[3]/div[1]/div/div/form/div[2]/fieldset[3]/div[4]/div/div/ul/li[2]").text
            print("alert INFO on page:", check_alert)
            if check_alert == read_config.load()['alert']:
                print("Still unavailable, sending noway email......")
                send_msg.noway()
            else:
                print("Now it's available, sending available email......")
                send_msg.available()
        except:
            print("Error in the third part => check alert message")
        finally:
            driver.quit()
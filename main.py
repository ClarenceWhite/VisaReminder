from datetime import datetime
from VisaReminder import VisaReminder

if __name__ == '__main__':
    #create a class object
    reminder = VisaReminder()

    while True:
        now = datetime.now()
        print("From main.py, now is:", now)
        minute = now.minute
        print("From main.py, now minute is:", minute)
        try:
            #run reminder every 59 minutes
            if minute % 1 == 0:
                print("From main.py, start run reminder......")
                reminder.RunReminder()
                print("From main.py, end run Reminder......")
        except Exception as e:
            print("Error in main.py:", e)

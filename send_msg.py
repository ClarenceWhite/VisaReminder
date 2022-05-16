from read_config import Config
import requests

read_config = Config()
api_url = read_config.load()['apikey']

no = {
    "title": "没有开放！",
    "desp": "目前还没有开始预约！"
}
yes = {
    "title": "开放预约！",
    "desp": "现在开放预约了！快去抢位置！"
}

class Wechat:
    def noway(self):
        x = requests.post(api_url, data = no)
        print(x.text)
    
    def available(self):
        x = requests.post(api_url, data = yes)
        print(x.text)
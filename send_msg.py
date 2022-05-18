from read_config import Config
import requests

read_config = Config()
api_url = read_config.load()['apikey']
appToken = read_config.load()['appToken']
uid = read_config.load()['uid']

no = { 'appToken': appToken,
            'content': '还是没有号，主人再等等看吧',
            'uid': uid}

yes = { 'appToken': appToken,
            'content': '终于有号啦！主人快去抢号鸭',
            'uid': uid}

chromeError = { 'appToken': appToken,
            'content': '呜呜呜，chrome程序可能出错了，服务器脚本失效！',
            'uid': uid}

mainError = { 'appToken': appToken,
            'content': '呜呜呜，main程序可能出错了，服务器脚本失效！',
            'uid': uid}

class Wechat:
    def noway(self):
        x = requests.get(api_url, params=no)
        print("noway text:\n", x.text)
    
    def available(self):
        x = requests.get(api_url, params=yes)
        print("available text:\n", x.text)

    def chromeError(self):
        x = requests.get(api_url, params=chromeError)
        print("chromeError text:\n", x.text)

    def mainError(self):
        x = requests.get(api_url, params=mainError)
        print("mainError text:\n", x.text)

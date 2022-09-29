import requests
import os

#用于仓库内脚本发送通知

########获取环境变量##########

CHAT_ID = os.getenv("TG_ID")
BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
BARK_KEY = os.getenv("BARK_PUSH")

##############################

def send_message(text):
    print(text,"\n")
    if len(BOT_TOKEN) != 0:    #telegram推送
        bot_data = {
            'chat_id': CHAT_ID,
            'text': text,
            'parse_mode': 'html'
        }
        url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
        rep = requests.post(url=url, data=bot_data)
        if rep.status_code != 200:
            print('telegram 推送失败')
        else:
            print('telegram 推送成功')
    if len(BARK_KEY) != 0:    #bark推送
        if "http" in BARK_KEY:
            rep = requests.get(BARK_KEY + "/" + text)
        else:
            rep = requests.get('https://api.day.app/' + BARK_KEY + "/" + text)
        if rep.status_code != 200:
            print('Bark 推送失败')
        else:
            print('Bark 推送成功')


'''
Author: fuwen 592409588@qq.com
Date: 2022-06-06 20:33:03
LastEditors: fuwen 592409588@qq.com
LastEditTime: 2022-06-06 21:42:16 
'''

import time
import requests
import json
import datetime

def send_ifttt_notice(event_name, key, *args):
    url = "https://maker.ifttt.com/trigger/{}/json/with/key/{}".format(event_name, key)
    text_dicts = {}
    for index, text in enumerate(args):
        text_dicts['val'+str(index+1)] = text
    # text_list = []
    # for text in args:
    #     text_list.append(text)
    # payload = {"value1": text_list[0], "value2": text_list[1], "value3": text_list[2]}
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, data=json.dumps(text_dicts), headers=headers)
    print(text_dicts)
    print(response.text)


# 面向对象
class SendIfttSMS():

    def __init__(self, event_anme, key) -> None:
        self.event_name = event_anme
        self.key = key
    
    def SendMessage(self, *args):
        url = "https://maker.ifttt.com/trigger/{}/json/with/key/{}".format(self.event_name, self.key)
        text_dicts = {}
        for index, text in enumerate(args):
            text_dicts['val'+str(index+1)] = text
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, data=json.dumps(text_dicts), headers=headers)
        return response


if __name__ == '__main__':
        
    Key = '**********************'          #这里填写上面小本本上记录的：秘钥 
    eventname = 'message_test' 
    text2 = '预警信息' + 'errormessage'
    text3 = '预警时间' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    send_ifttt_notice(eventname, Key, text2, text3) # 这里第一个参数，就是上边小本本上记录的：名称A 

    time.sleep(3)
    FirstIftt = SendIfttSMS(event_anme=eventname, key=Key)
    FirstIftt.SendMessage(text2, text3)



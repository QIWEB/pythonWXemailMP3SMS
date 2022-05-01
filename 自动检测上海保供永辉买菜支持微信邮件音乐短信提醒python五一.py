#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 06
# @Author  : qiweb
# @Software: PyCharm
# 大家劳动节快乐 送给上海 抢菜的人
# 不可用于非法用途，使用本程序所产生的后果，与本人概不相关。
#上海买菜太难了   送给你

'''
#安装下面imprt 第三方库 方法
#pip3 install pygame -i https://pypi.tuna.tsinghua.edu.cn/simple
#pip3 install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl

解放双手｜利用 PyAutoGUI 快速构建自动化操作脚本
简单地说， PyAutoGUI 就是模拟键盘、鼠标在界面上进行操作的包。安装时直接使用如下语句：

pip install pyautogui即可。

编写一个简单的测试程序：

import pyautogui as pagpag.PAUSE = 1.5pag.click(63,191)

pyperclip模块中有两个函数，分别是copy()和paste()，copy()用于向计算机的剪贴板发送文本，paste()用于从计算机剪贴板接收文本。

Pygame 是一个专门用来开发游戏的 Python 模块
用它播放提示音乐
'''
import requests
import random
import socket
import struct

import pyautogui as pg
import pyperclip as pc

import json
import sys
import time

import pygame  #需要下载 pip install pygame

#pip install pygame

#播放音乐的路径  电脑提醒
filepath=r'Are You Ok！.mp3'

#提示音多长时间
ss=20

#随机这个范围的时间重试 访问网页  秒
startx=80
endx=308

#作为发送放账号
mail_user1 = '改参数'
# 密码(部分邮箱为授权码)
mail_pass1 = '改参数'
# 邮件发送方邮箱地址
sender1 = '改参数@163.com'
# 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['改参数@qq.com']

#接收短信通知
myphone="改参数"
#日志文件
log_file="cailog2.txt"



def log_print(*objects, sep=' ', end='\n', file=None):
    #print("当前时间：" + datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 这样每次调用log_print()的时候，会先输出当前时间，然后再输出内容
    # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    print(*objects, sep=' ', end='\n', file=log_file)

class Logger(object):
    def __init__(self, fileN='Default.log'):
        self.terminal = sys.stdout
        sys.stdout = self
        self.log = open(fileN, 'w')

    def write(self, message):
        '''print实际相当于sys.stdout.write'''
        self.terminal.write(message)
        self.log.write(message)

    def reset(self):
        self.log.close()
        sys.stdout = self.terminal

    def flush(self):
        pass

#
def  sendEmail(TEXTX,youcai,now02):
    import smtplib
    from email.mime.text import MIMEText

    # 设置服务器所需信息
    # 163邮箱服务器地址
    mail_host = 'smtp.163.com'
    # 163用户名
    mail_user = mail_user1
    # 密码(部分邮箱为授权码)
    mail_pass = mail_pass1
    # 邮件发送方邮箱地址
    sender = sender1
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    receivers = ['908701702@qq.com']

    # 设置email信息
    # 邮件内容设置
    message = MIMEText('小程序抢菜\n' + TEXTX, 'plain', 'utf-8')

    import datetime

    i = datetime.datetime.now()
    print("当前的日期和时间是 %s" % i)
    print(str(i).replace("-", "").replace(":", "").replace(".", ""))

    # 邮件主题
    message['Subject'] = '永辉菜' + youcai + now02
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误

#初始化
#播放音乐  文件  播放多少秒
def PlayMusic(filepath,ss):

    pygame.mixer.init()

    #加载音乐

    track=pygame.mixer.music.load(filepath)

    #播放

    pygame.mixer.music.play()

    #暂停

    time.sleep(ss)

    #返听 点播放后继续播放

    #pygame.mixer.music.pause()

    #停止

    pygame.mixer.music.stop()
#发送永辉查下请求
def post_data(title, content):
    url = 'https://api.yonghuivip.com/webapi/cms-activity-rest/h5/activity/page?platform=wechatminiprogram&v=8.4.6.15&channel=512&distinctId=872028242588383208&proportion=1&screen=1920*1080&pagesize=6&networkType=wifi&aid=625ea1799eebbd00060f99cb&appType=h5&model=microsoft&os=windows&osVersion=Windows+11+x64&channelSub=&brand=microsoft&productLine=YhStore&access_token=ec36827ed0f6bfaaf36e16e3f3c632212eba4087ef47d3e99fe9658bca8977e89f8879fe53ef190cdc55f973b22fab9935886f5bea57998aa303e175a3ee052e3fe86ceea87a11ae25333942948d8134-601933-vTBJu2qyEJ84jhS7lOHMmJx5jSK8ZCoAZumHqa5_URI0bD5AeCGSSCBvWvy61rPP&appid=wxc9cf7c95499ee604&uid=872028242588383208&deviceid=835b16e9-dc05-4e5b-afdd-979ebe9c17e7&sellerid=7&shopid=9696&showmultiseller=%7B%227%22:%229696%22%7D&sellername=%E6%B0%B8%E8%BE%89%E8%B6%85%E5%B8%82&shopname=%E5%94%90%E9%95%87%E9%98%B3%E5%85%89%E5%9F%8E%E5%BA%97&ppname=%E9%A6%96%E9%A1%B5&userid=872028242588383208&currentclientid=&skipclientid=&timestamp=1651324558174&sign=7648675b30b51795a907b2e2b15d3c77'
    data = json.dumps({'title': title,'content': content})
    headers = {
        'Host': 'api.yonghuivip.com',
        'Connection': 'keep-alive',
        "X-YH-Biz-Params":"gib=-_-0'')))!,*)_!('&gvo=+-0_$,),'-,),_$)_&ncjkdy=,','&nzggzmdy=(&xdotdy=-",
    'Accept': 'application/json, text/plain, */*',
    'X-YH-Context': 'origin=h5&morse=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cmsh5.yonghuivip.com/index.html?canShare=1&needlocation=1&showLoading=0&aid=625ea1799eebbd00060f99cb&isForward=0&token=ec36827ed0f6bfaaf36e16e3f3c632212eba4087ef47d3e99fe9658bca8977e89f8879fe53ef190cdc55f973b22fab9935886f5bea57998aa303e175a3ee052e3fe86ceea87a11ae25333942948d8134-601933-vTBJu2qyEJ84jhS7lOHMmJx5jSK8ZCoAZumHqa5_URI0bD5AeCGSSCBvWvy61rPP&unionId=oCjU7wH_eq18p5BnslgqUz8SX8PE&cityid=1&lng=121.6688849582476&lat=31.20989619892082&addressId=57653861&appid=wxc9cf7c95499ee604&v=8.4.6.15&fromorigin=miniprogram&mobile=15889723562&deviceid=835b16e9-dc05-4e5b-afdd-979ebe9c17e7&platform=windows&userid=872028242588383208&sellerid=7&shopid=9696&sellername=%E6%B0%B8%E8%BE%89%E8%B6%85%E5%B8%82&shopname=%E5%94%90%E9%95%87%E9%98%B3%E5%85%89%E5%9F%8E%E5%BA%97&scDistinctId=872028242588383208&FPName=&PPName=%E9%A6%96%E9%A1%B5&sceId=1001&opId=oP_Ic0RzjQNrsxoeQDPdTy0g7re0&project_name=yh_life&pub_v=19&yh_appName=%E6%B0%B8%E8%BE%89%E7%94%9F%E6%B4%BB&trace_id=1651324239189%5ExB37jccH&span_id=1651324557236201&mid=Default&sid=Default&cid=Default&showmultiseller=%7B%227%22%3A%229696%22%7D&brand=microsoft&model=microsoft&os=windows&osVersion=Windows%2011%20x64&screen=414*736&productLine=YhStore&channelSub=&appType=mini&proportion=1&networkType=wifi&channel=512',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-us,en',
    'Cookie': 'sajssdk_2015_cross_new_user=1; userKey=ec36827ed0f6bfaaf36e16e3f3c632212eba4087ef47d3e99fe9658bca8977e89f8879fe53ef190cdc55f973b22fab9935886f5bea57998aa303e175a3ee052e3fe86ceea87a11ae25333942948d8134; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221807a985ae28c-06d408b57b8a4a-16017334-2073600-1807a985ae381e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgwN2E5ODVhZTI4Yy0wNmQ0MDhiNTdiOGE0YS0xNjAxNzMzNC0yMDczNjAwLTE4MDdhOTg1YWUzODFlIiwiJGlkZW50aXR5X2Fub255bW91c19pZCI6Ijg3MjAyODI0MjU4ODM4MzIwOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221807a985ae28c-06d408b57b8a4a-16017334-2073600-1807a985ae381e%22%7D'
    }


    response = requests.post(url, data, headers=headers)
    return str(response.text)

#解析蔬菜列表
def infox(shucai):
    #print(type(shucai))
    if  "title" not in shucai:
        if "name" in shucai:
            return shucai["name"]
        return ""
    # 套餐名称
    title = shucai["title"]
    # 已售完
    actiontext = shucai["cartAction"]["actionText"]
    # 已售22423份
    presaleInfo = shucai["presaleInfo"]["soldVolDesc"]
    # 价格
    price = shucai["price"]["price"]
    # 时间
    now = int(round(time.time() * 1000))
    now02 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
    #print(now02)
    #print(title, actiontext, presaleInfo, price, '元')
    return (actiontext,price+"元",title, presaleInfo)



#API接口初始化，按照手机号生成不同的网址
def initAPI(phone):
    # 短信接口API 请求间隔时间 备注 请求方式 请求参数 需要SESSION的先决请求URL以及Referer
    APIList = [
        [
            "http://reg.ztgame.com/common/sendmpcode?source=giant_site&nonce=&type=verifycode&token=&refurl=&cururl=http://reg.ztgame.com/&mpcode=&pwd=&tname=&idcard=",
            60, "巨人网络", "GET", {'phone': phone}, "http://reg.ztgame.com/"],

        ["https://www.decathlon.com.cn/zh/ajax/rest/model/atg/userprofiling/ProfileActor/send-mobile-verification-code",
         30,
         "迪卡侬", "POST", {"countryCode": "CN", "mobile": phone}, "https://www.decathlon.com.cn/zh/create"]

    ]
    return APIList

# 短信初始化
class initSMS(object):
    """docstring for initSMS"""

    def __init__(self):
        super(initSMS, self).__init__()
        self.SMSList = []
        self.intervalInfo = 0

    def initBomb(self,APIList):
        for x in APIList:
            self.intervalInfo += 1
            self.SMSList.append(SMSObject(x[0], x[1], x[2], x[3], x[4], x[5], self.intervalInfo))
        return self.SMSList


class SMSObject(object):
    """docstring for SMSObject"""  # __var 私有成员变量

    def __init__(self, url, interval, info, method, params, others, intervalInfo):
        super(SMSObject, self).__init__()
        self.__url = url
        self.__interval = interval
        self.__info = info
        self.__intervalInfo = intervalInfo
        self.__method = method
        self.__params = params
        self.__others = others

    def getUrl(self):
        return self.__url

    def getInfo(self):
        return self.__info

    def getParams(self):
        return self.__params

    def getMethod(self):
        return self.__method

    def getOthers(self):
        return self.__others

    def getInterval(self):
        return self.__interval

    def getintervalInfo(self):
        return self.__intervalInfo

    def setintervalInfo(self, intervalInfo):
        self.__intervalInfo = intervalInfo


class Bomb(object):
    """docstring for Bomb"""

    def __init__(self):
        super(Bomb, self).__init__()
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
            'Referer': 'http://10.13.0.1',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh-TW;q=0.8,zh;q=0.6,en;q=0.4,ja;q=0.2',
            'cache-control': 'max-age=0',
            "X-Requested-With": "XMLHttpRequest"
        }

    def send(self, SMS):
        # return "SUCCESS"
        IP = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        self.HEADERS['X-FORWARDED-FOR'] = IP
        self.HEADERS['CLIENT-IP'] = IP
        try:
            session = requests.Session()
            if SMS.getOthers() != "":
                session.get(SMS.getOthers(), timeout=5, headers=self.HEADERS)
                self.HEADERS['Referer'] = SMS.getOthers()
            if SMS.getMethod() == "GET":
                req = session.get(SMS.getUrl(), params=SMS.getParams(), timeout=5, headers=self.HEADERS)
            else:
                req = session.post(SMS.getUrl(), data=SMS.getParams(), timeout=5, headers=self.HEADERS)
        # print(req.url)
        except Exception as e:
            return str(e)
        return "已发送"


def sendSMS(phone):
    APIList=initAPI(phone) # API接口初始化
    print("\n电话：", phone)
    SMSList = initSMS().initBomb(APIList=APIList)
    switchOn = Bomb()
    i = 0
    for x in SMSList:
        i += 1
        info = switchOn.send(x)
        print(str(i) + "." + x.getInfo() + " " + info)




#发送微信通知
class SendWxMsg(object):

    def __init__(self):
        self.name = '文件传输助手'
        #self.name = 'qiweb3'
        self.msg = '自动发微信消息'

    def send_msg(self,msgs):
        self.msg=msgs
        # 操作间隔为1秒
        pg.PAUSE = 1.5
        pg.hotkey('ctrl', 'alt', 'w')
        pg.hotkey('ctrl', 'f')

        # 找到好友
        pc.copy(self.name)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')


        # 发送消息
        pc.copy(self.msg)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # 隐藏微信
        time.sleep(1)
        pg.hotkey('ctrl', 'alt', 'w')

'''
测试 音乐和手机通知
PlayMusic(filepath, ss)
print("正在发送短信提醒。。。")
sendSMS(myphone)
s=SendWxMsg()
s.send_msg("测试wx")
sendEmail("测试短信", youcai, now02)
'''



# 入口 程序
while True:
    logger = Logger('cailog.txt')
    now = int(round(time.time() * 1000))
    now02 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
    # 随机
    xtime = random.randint(600, 1500)
    xtime = random.randint(startx, endx)
    print(xtime, "秒后开始执行 ", now02)
    time.sleep(xtime)
    now = int(round(time.time() * 1000))
    now02 = time.strftime('%H', time.localtime(now / 1000))
    if int(now02) >= 6:
        print("点6后开始抢了")
    else:
        print("6点前休息等待ing")
        continue

    rsp = post_data("", "")
    print(rsp)
    jsontext = json.loads(rsp)
    # 获得蔬菜
    shucai = jsontext["data"]["floors"][5]["value"][0]
    # 套餐名称
    title = shucai["title"]
    # 已售完
    actiontext = shucai["cartAction"]["actionText"]
    # 已售22423份
    presaleInfo = shucai["presaleInfo"]["soldVolDesc"]
    # 价格
    price = shucai["price"]["price"]
    # 时间
    now = int(round(time.time() * 1000))
    now02 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
    print(now02)
    print(title, actiontext, presaleInfo, price, '元')

    youcai = "没有了"
    print("状态" + actiontext)
    # PlayMusic(filepath,ss)
    if actiontext not in u"已抢完 ，08:30-19:00\n开始售卖":
        print("蔬菜有货了 发邮件快抢 mp3提醒")
        PlayMusic(filepath, ss)
        print("正在发送短信提醒。。。")
        sendSMS(myphone)
        try:
            # 微信
            s = SendWxMsg()
            s.send_msg(now02 + "-通知：" + TEXTX)
        except:
            print("exception")

        youcai = "蔬菜有货了"

    TEXTX = ""

    shucaiz = jsontext["data"]["floors"]
    for z in shucaiz:
        y = z["value"]
        # print(type(z["value"]),isinstance(y,list))
        if isinstance(y, list):
            for x in y:
                TEXTX += str(infox(x)) + "\n"

    '''
        #保供套餐
        shucaix=jsontext["data"]["floors"][5]["value"]


        for x in shucaix:
            TEXTX+=str(infox(x))+"\n"
        #其他商品
        shucaiy=jsontext["data"]["floors"][6]["value"]
        for x in shucaiy:
            TEXTX+=str(infox(x))+"\n"
    '''
    # 时间
    now = int(round(time.time() * 1000))
    now02 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
    # log_print(now02)
    # log_print(TEXTX)
    print(TEXTX)
    # logger.reset()
    # logger.write(TEXTX)
    sendEmail(TEXTX, youcai, now02)

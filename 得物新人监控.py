import requests
from fake_useragent import UserAgent

token = '126c2e9648f244ba91ac33a03a6e1bde'
ua = UserAgent().random
消息内容 = ''


# print(ua)
# 有时需要在请求中添加转义字符,可能请求体中的像是字典,实际上是一个字符串
def 推送():
    global token
    data = {
        "token": token,
        "title": "得物商品到货了!!!!!",
        "content": 消息内容,
        # "topic":"test"
    }
    headers = {
        'USER-AGENT': ua
    }

    url = "http://www.pushplus.plus/send/"
    res = requests.post(url=url, data=data, headers=headers)
    # print(res.json())


def 得物商品监控():
    url = 'https://app.dewu.com/hacking-newbie/v1/high-value/allowance-module?sign=f483f265e919adbd19aa29758394d28d'
    headers = {
        'Host': 'app.dewu.com',
        'Connection': 'keep-alive',
        'ua': 'duapp/5.22.3(android;11)',
        'appid': 'h5',
        'SK': '9JgSKkxfRab52YsrdOjH54LecF84HNlf5diZf1Bar21LuO2dT61f7BMr3jx71zpgBz2FenzLWbqdN4ucytOKTa9FJr1u',
        'shumeiId': '202206201105599577aec2d8302d653009c385871e64ef01dab1c9dbe482cd',
        'deviceTrait': 'Redmi+Note+8+Pro',
        'x-auth-token': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2OTE4OTc3MjIsImV4cCI6MTcyMzQzMzcyMiwiaXNzIjoiZGY2NmU1MDhmM2JjZmZkMyIsInN1YiI6ImRmNjZlNTA4ZjNiY2ZmZDMiLCJ1dWlkIjoiZGY2NmU1MDhmM2JjZmZkMyIsInVzZXJJZCI6MTkzMTk0ODA5NywidXNlck5hbWUiOiLlvpfniallci0xSzRRNE04QyIsImlzR3Vlc3QiOmZhbHNlfQ.Ed3s-Om1NfYLpLfAlZmKjhPXFGjauVgCaTzurk_0aNd9DLDrxSAmEISb1kcqGENG0o9k4TXbFuw4OKvXFneATxkRYa9Z-b3rtBJyBh3YJvD5jWIM0DE0yggjuEWC7aTGEdjKc4hWlyOXcIeqQ1LUQ4-wPty-y6vUb1jYMMyuNHpUIQUArMWRz6jrUVZIKuZEujCwQCvgEnIjjmc4dUFC-fgy4J95FPT36jcq7BSmNzsf9xmjvRTnu8DX-FNvkfP11yZaHXQX3ujrO97CBCZurzuGAVbp3UCYY_uflgcFpPbudzYYGBQ8XZgTYg2sZ9ARhndWT95qIZI8ZqgfRXwJJA',
        'uuid': 'df66e508f3bcffd3',
        'channel': 'du',
        'duToken': 'd41d8cd9|1931948097|1691896335|b5af6a3a7707b4de',
        'appVersion': '5.22.3',
        'emu': '0',
        'cookieToken': 'd41d8cd9|1931948097|1691896335|b5af6a3a7707b4de',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36/duapp/5.22.3(android;11)',
        'isRoot': '0',
        'imei': '',
        'platform': 'h5',
        'isProxy': '0',
        'Accept': '*/*',
        'Origin': 'https://m.dewu.com',
        'X-Requested-With': 'com.shizhuang.duapp',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.dewu.com/h5-newbie/super-deal-product',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'duToken=d41d8cd9|1931948097|1691896335|b5af6a3a7707b4de',
        'Content-Type': 'application/json'
    }
    data = {"pageSize": '52', "lastSpuId": '5479197'}
    payload = "{\"pageSize\":52,\"lastSpuId\":5479197}"
    res = requests.post(url=url, data=payload, headers=headers)
    # print(res.json())
    res_json = res.json()
    list0 = res_json["data"]["spuList"]
    for i in list0:
        if i['discountPrice'] <= 3000 and i['status'] == 11:
            # print(i)
            global 消息内容
            消息内容 += i['spuName'] + '价格=' + str(int(i['discountPrice']) / 100) + '\n'
    print(消息内容)
    推送()

    # for i in list0:
    #     if i['discountPrice'] <= 4000 and i['status'] == 11:
    #         # print(i)
    #         global 消息内容
    #         消息内容 = i['spuName'] + '价格=' + str(int(i['discountPrice']) / 100) + '\n'
    #         消息内容 += 消息内容
    #         print(消息内容)


# 推送()

if __name__ == '__main__':
    得物商品监控()

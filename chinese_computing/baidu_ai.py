# -*- encoding:utf-8 -*-

import requests
import json
#
# url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token=24.e9cd7b2fd40db3bdc2874b7987562ef0.2592000.1542441622.282335-14470681"
# header = {'Content-Type': 'application/json', 'charset': 'utf-8'}
# s = json.dumps({"text": "你是好人"}).encode('gbk')
# r = requests.post(url, s)
# print(r.text.encode('utf-8'))
# 6xjkB2bFjfwt1QhuG%2Bzz6NwpR0RX%2BxsBR9G3U8%2BwadE%3D
# wenzhi.api.qcloud.com/v2/index.php?Action=TextSentiment&content=老子就是喜欢吃火锅，关你锤子事&Nonce=345122&Region=sz&SecretId=AKIDPhpodG7060iEZkrX9aCfw2wgFcos4PtB&SignatureMethod=HmacSHA256
url = "https://wenzhi.api.qcloud.com/v2/index.php?Action=TextSentiment&content=how are you&Nonce=345122&Region=sz&SecretId=AKIDPhpodG7060iEZkrX9aCfw2wgFcos4PtB&Signature=BDOSsZ9NbrFfGKJUNpkH65xfRs4fXIEq4TXXN4%2BdN8E%3D"
# header = {'Content-Type': 'application/json', 'charset': 'utf-8'}
r = requests.get(url)
print(r.text)

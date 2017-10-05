import urllib.request   #请求访问url的包
import urllib.parse     #负责解析的包

url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='

'''
head = {}       #dict
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
'''

#Form表单
data = {}
data['i'] = 'I love Python'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1505821579753'
data['sign'] = 'f4ff939bbaf67c8d83efd17ee8d82c0b'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')     #编码

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')       #解码为unicode

print(html)

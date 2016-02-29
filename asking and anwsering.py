import requests
import urllib

import re
#
def getbaike(html):
    p=re.compile(r'"http://www\.baidu\.com/link\?url=(.*) target="_blank"')
    baike=re.findall(p,html)
    return baike
def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)
def getcontent(baikepage):
    p=re.compile(r'content="(.*)">')
    content=re.findall(p,baikepage)
    return content             
def search():
 print "魔镜：我是魔镜上至三百年，后知三百年："
 print "魔镜：你究竟想知道什关于世界上哪个东西的事情:"
 searchitem=raw_input("我：")
 payload={'wd':searchitem,'rn':'200'}
 #百度搜索的参数
 web=requests.get("http://www.baidu.com/s",params=payload)

 page=urllib.urlopen(web.url)
 #print web.url
 html=page.read()
 baike=getbaike(html)
 #得到匹配的百度百科后缀
 baike[0]=DelLastChar(baike[0])
 #print baike[0]
 baike[0]=str(baike[0])
 baikeurl='www.baike.baidu.com/link?url='+baike[0]
 #print baikeurl
 baikepage=gethtml('http://'+baikeurl)
 content=getcontent(baikepage)
 if content:
     print "魔镜：这是你要的答案："
     result=''.join(content[0])
 
     print result
 else:
     print "魔镜：竟然连我也不知道？what the fuck!"

while 1:
    search()

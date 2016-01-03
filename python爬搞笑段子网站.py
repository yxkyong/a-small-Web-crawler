# a-small-Web-crawler
a small Web crawler by python 
import sys
import re
import urllib
#返回html格式
def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
 
def getmessage(html):
    p=re.compile(r'<div class="content">(.*)</div><script type="text/javascript">')
    #对段子内容进行正则匹配
    message=re.findall(p,html)#返回正则匹配的结果
    return message
fp=open('data.txt','w+')
#实际范围比1~7000要大，因为时间原因这里暂定为1~7000
for i in range(1,7000):
   i=str(i)
   web=gethtml('http://ishuo.cn/subject/'+i)
   #该网站段子的链接特点
 
   message=getmessage(web)
 
   message2=''.join(message)#将结果转换为字符串类型
   #message2=message2.decode('utf8','strict')
   message2=str(message2)
   print message2
   
    
   fp.writelines(message2+'\n')
   #将爬下的众多段子写入文件中
 
 
fp.close()

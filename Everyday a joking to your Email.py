#using SMTP and a crawler 
#1
#send an Email to yours
import sys
import re
import urllib
import smtplib
import random
from email.mime.text import MIMEText 
 
to=['duem123321@163.com']
host="smtp.163.com"  #smtp服务器
user="duem123321"    #用户名
password="******"   #密码
postfix="163.com"  #后缀
def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
 
def getmessage(html):
    p=re.compile(r'<div class="content">(.*)</div><script type="text/javascript">')
    #对段子内容进行正则匹配
    message=re.findall(p,html)#返回正则匹配的结果
    return message
def send_mail(to_list,sub,content): 
    me="段子集中营"+"<"+user+"@"+postfix+">" 
    msg = MIMEText(content,_subtype='plain',_charset='gb2312') 
    msg['Subject'] = sub 
    msg['From'] = me 
    msg['To'] = ";".join(to_list) 
    try: 
        server = smtplib.SMTP() 
        server.connect(host) 
        server.login(user,password) 
        server.sendmail(me, to_list, msg.as_string()) 
        server.close() 
        return True 
    except Exception, e: 
        print str(e) 
        return False 
if __name__ == '__main__':
    i=random.randint(1,500)
    i=str(i)
    web=gethtml('http://ishuo.cn/subject/'+i)
    #该网站段子的链接特点
 
    message=getmessage(web)
 
    message2=''.join(message)#将结果转换为字符串类型
     
    #message2=message2.decode('utf8')
    message2=str(message2)
    print message2  
    if send_mail(to,"每天一则搞笑段子",message2): 
        print "Suceed!" 
    else: 
        print "Failed!"

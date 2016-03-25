#coding:utf-8

import re
import urllib
import string
import matplotlib.pyplot as plt
import numpy as np
def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getdata(html,number):
    p=re.compile(r'<td><a href="http://data.eastmoney.com/bbsj/'+number+'.html" target="_blank">(.*)</td>')
    datalist=re.findall(p,html)
    return datalist


def manage():
    number=raw_input('Code:')
    web=gethtml('http://quote.eastmoney.com/sz'+number+'.html') 
    managelist=[]
    firstlist=getdata(web,number)
    numberlist1=[]
    numberlist2=[]
    numberlist3=[]
    for i in range (1,4):
        managelist.append(firstlist[-i])
    str1=str(managelist[0])
    for i in range (2,10):
        if str1[-i]=='\xba':
            break
        numberlist1.append(str1[-i])
    str2=str(managelist[1])
    for i in range (2,10):
        if str1[-i]=='\xba':
            break
        numberlist2.append(str2[-i])
    str3=str(managelist[2])
    for i in range (2,10):
        if str3[-i]=='\xba':
            break
        numberlist3.append(str3[-i])
    in_par=string.atof(''.join(numberlist1[::-1]))
    win_par=string.atof(''.join(numberlist2[::-1]))
    jud_self=string.atof(''.join(numberlist3[::-1]))
    plt.title('Company core data of Code'+number)
    dict = {'year basis': jud_self, ' gross profit rate;': win_par, 'ROE': in_par}
    for i ,key in enumerate(dict): plt.bar(i,dict[key])
    plt.xticks(np.arange(len(dict))+0.4,dict.keys())
    plt.yticks(dict.values())
    plt.show()
if __name__ == '__main__':
    manage()
    




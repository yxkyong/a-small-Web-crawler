import re
import urllib

def gethtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html


def getimg(html):
    p=re.compile(r'"http://pic\.(.*)\.jpg"')
    imglist=re.findall(p,html)
    return imglist

web=gethtml('http://www.222lu.us/')
step=re.compile(r'"/vodlist/(.*)\.html"')
urllist=re.findall(step,web)
name = 100
print urllist
for urlstep in urllist:
  urlstep2='http://www.222lu.us/vodlist/'+urlstep+'.html'
  print urlstep2
  web=gethtml(urlstep2)
  imglist=getimg(web)
  print imglist
  for imgurl in imglist:
     urllib.urlretrieve("http://pic."+imgurl+'.jpg','F:\\img\%s.jpg'%name)
     name+=1

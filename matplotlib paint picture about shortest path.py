#the data come from C-DATA-STURCTURE about shortest path problem#
#draw the picture
#using matplotlib
import matplotlib.pyplot as plt
from numpy import *
import re
fp=open("out.txt","r")
txt=fp.readline()
p=re.compile(r'(.,.)')
plist=re.findall(p,txt)
xlist=[]
ylist=[]
#A\B\C\D\E\的初始坐标
gridlist=array([[30.0,30.0],[20.0,40.0],[60.0,50.0],[20.0,10.0],[37.0,6.0]])
 
for i in range(4):
    x0=gridlist[ord(plist[i][0])-48][0]
    y0=gridlist[ord(plist[i][0])-48][1]
    x1=gridlist[ord(plist[i][2])-48][0]
    y1=gridlist[ord(plist[i][2])-48][1]
    if(x0<=x1):
      x=arange(x0,x1,0.01)
       
     
      y=((y0-y1)/(x0-x1))*x+(y0-(y0-y1)/(x0-x1)*x0)
    else:
          x=arange(x1,x0,0.01)
          y=((y0-y1)/(x0-x1))*x+(y0-(y0-y1)/(x0-x1)*x0)
     
     
    xlist.append(x)
    ylist.append(y)
 
#plt.grid(True)
print plist
print xlist
plt.annotate('A', xy = (30, 30), xytext = (30,30), \
arrowprops = dict(facecolor = 'black', shrink = 0.1))
plt.annotate('B', xy = (20, 40), xytext = (20,40), \
arrowprops = dict(facecolor = 'black', shrink = 0.1))
plt.annotate('C', xy = (60, 50), xytext = (60,50), \
arrowprops = dict(facecolor = 'black', shrink = 0.1))
plt.annotate('D', xy = (20, 10), xytext = (20,10), \
arrowprops = dict(facecolor = 'black', shrink = 0.1))
plt.annotate('E', xy = (37, 6), xytext = (37,6), \
arrowprops = dict(facecolor = 'black', shrink = 0.1))
plt.plot(xlist[0],ylist[0],xlist[1],ylist[1],xlist[2],ylist[2],xlist[3],ylist[3])
plt.show()

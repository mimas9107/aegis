import os
from bs4 import BeautifulSoup
import lxml
import datetime
import time

filename='AaFish-20250121-output.gpx'

with open(filename,'r') as f:
    buf=f.read()


soup=BeautifulSoup(buf,'lxml')
trk=soup.find('trk')

n_trkpt=len(trk.find_all('trkpt'))
print(n_trkpt)

with open(filename,'r') as f:
    bufs=f.readlines()

with open('testout.txt','w') as f2:
    l=0
    c=0
    # t0=datetime.datetime.now()
    t0=datetime.datetime(2025, 1, 18, 7, 0, 0, 0)
    t=t0
    for e in bufs:
        print(l, e)
        
        if('time' in e):
            t=t+datetime.timedelta(seconds=1)
            # print(e[6:26], t.isoformat()[0:19]+'Z')
            newtime:str='<time>'+t.isoformat()[0:19]+'Z</time>'
            f2.write(newtime+'\r')
            c+=1
        else:
            f2.write(e)
        l+=1
            
    print(t-t0)

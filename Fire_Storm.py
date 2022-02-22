# Fire Storm
import requests,sys,os
from bs4 import BeautifulSoup
from colorama import Fore
from time import sleep
print(Fore.YELLOW+'''
10101010    01
10          
01001011    01    0 0111      0000
10          01    10         0    1
01          01    0         11111111
01          10    1         1
                             000000
          10           000                         
  1111 11111000       0   0        1 0111    1               
  1       00          0   0        10        000000000              
  1       10          0   0        1         1   1   1
  111     01          0   0        1         0   1   1
    1     10           000         1         1   0   0          
 1111     
          
''')           


print(Fore.RED+'[1] brut force')
sleep(0.2)
print(Fore.GREEN+"[2] scrapy")
sleep(0.2)
print(Fore.BLUE+"[3] Scanner")
sleep(0.2)
print("[4] whois")
sleep(0.2)
print(Fore.YELLOW+"[5] exit")
print(Fore.RED+"please Enter your option")
option=input(Fore.YELLOW+"|__》")
def exist():
    sys.exit()   
def brut_force():
    try:
        lst=["aaaa","login"]
        print(Fore.RED+"please Enter your site")
        url=input(Fore.BLUE+"|__》")
        wor = url.split() 
        r = ' '.join(wor)
        url=r
        if "http" in url:
            pass
        elif "http" != url:
            url=("http://"+url)
        for i in lst:
            ur=(url+"/"+i)
            reqs=requests.get(ur)
            if reqs.status_code==200:
                print(Fore.GREEN+"[+] "+ur)
            else:
                print(Fore.RED+"[-] "+ur)
        
    except:
        print(Fore.RED+"please Enter your site again")
        exist()
        
        
def scrapy():
    try:
        print("please Enter your site")             
        scrapy_ur=input(Fore.BLUE+"|__》")
        word = scrapy_ur.split() 
        ress = ' '.join(word)
        scrapy_ur=ress
        print(Fore.RED+"please Enter tag name")
        tag=input(Fore.BLUE+"|__》")
        wordss = tag.split() 
        resss = ' '.join(wordss)
        tag=resss
        if "http" in scrapy_ur:
            pass
        elif "http" != scrapy_ur:
            scrapy_ur=("http://"+scrapy_ur)
        
        requ=requests.get(scrapy_ur)
        soup=BeautifulSoup(requ.text,"html.parser")
        data=soup.findAll("{}".format(tag))
        for i in data:
            print(i)
    except:
        print(Fore.RED+"please Enter url and tag name again")
def Scanner():
    print(Fore.GREEN+"[3] sql injection") 
    print(Fore.RED+"[2] xss")
    print(Fore.BLUE+"[1] LFI")
    
    
def whois():
    try:
        temp=[]
        print(Fore.RED+"please Enter your site target")
        ur_whois=input("|__》")
        words = ur_whois.split() 
        res = ' '.join(words)
        ur_whois=res
        if "http" in ur_whois:
            print(Fore.RED+"please Enter url     without"+Fore.BLUE+"http or https")
            exist()
        elif "http" != ur_whois:
            pass
                
        req_whois=requests.get("http://who.is/whois/"+ur_whois)
        soup_whois=BeautifulSoup(req_whois.text,"html.parser")
        data_whois=soup_whois.findAll("pre")
        for i in data_whois:
            temp.append(i)
        filename=("whois_{}".format(ur_whois)+".html")
        fileopen=open(filename,"w+")
        for i in temp:
            fileopen.write(str(i))
            print(Fore.GREEN+"saved file directory》namefile:{}".format(filename))
    except:
        print(Fore.RED+"please Enter site again")    
        
if option=="5":
    exist()
elif option=="1":
    brut_force()
elif option=="2":
    scrapy()
elif option=="3":
    Scanner()
elif option=="4":
    whois()    
    
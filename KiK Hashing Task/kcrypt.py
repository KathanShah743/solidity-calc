import random

def gensalt(id:str,pass1:str):
    length = len(pass1)
    poww = 9 - length
    lo = 10**poww
    hi = 10*lo - 1
    salt = str(random.randint(lo,hi))
    return salt

def genhash(pass1:str,newsalt:str):
    newpass = pass1 + newsalt
    theHash = ''
    num = 0
    power = 1
    for char in newpass:
        num = num + (100*(1+(ord(newsalt[ord(char)%4]))%9) - 30 - 10*(1+(ord(newsalt[ord(char)%4]))%4) + ord(char))*power
        power = power*1000
    theHash = str(hex(num))
    return theHash
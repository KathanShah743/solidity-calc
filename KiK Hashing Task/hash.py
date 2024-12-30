import json
import kcrypt

def updatepwd(id, new_data, filename='pwd.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data[id] = new_data
        file.seek(0)
        json.dump(file_data,file,indent=4)

def updateslt(id, new_data, filename='slt.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data[id] = new_data
        file.seek(0)
        json.dump(file_data,file,indent=4)

def checkid(id:str):
    with open('pwd.json','r') as openfile:
        json_obj = json.load(openfile)
        if id in json_obj.keys():
            return 1
        else:
            return 0
        
def checkpwd(id:str,newp:str):
    with open('pwd.json','r') as pfile:
        json_pwd = json.load(pfile)
        if json_pwd[id]==newp:
            return 1
        else:
            return 0
        
def findslt(id:str):
    with open('slt.json','r') as sfile:
        json_slt = json.load(sfile)
        return str(json_slt[id])

def signup():
    id = input('Enter your username: ')
    if checkid(id):
        print('Username already registered. Please Log In.')
        return 0
    else:
        pass1 = input('Enter password (4-6 characters): ')
        if len(pass1)>6 or len(pass1)<4:
            print('Password must be of 4-6 characters only.')
            return 0
        else:
            genersalt = kcrypt.gensalt(id, pass1)
            updatepwd(id, kcrypt.genhash(pass1, genersalt))
            updateslt(id, genersalt)
            print('You have successfully registered! Thank You.')
            return 0

def login():
    id = input('Enter your username: ')
    if not checkid(id):
        print('Username not registered. Please Sign Up first.')
        return 0
    else:
        passw = input('Enter your password: ')
        newp = kcrypt.genhash(passw,findslt(id))
        if checkpwd(id,newp):
            print('You have logged in successfully! Thank You.')
            return 0
        else:
            print('Incorrect Password. Please try again.')
            return login()

flag = 1
while(flag):
    print('Enter 1 to Sign Up')
    print('Enter 2 to Log In')
    print('Enter $ to Quit Program')
    opt = input()
    if opt=='1':
        flag = signup()
    elif opt=='2':
        flag = login()
    elif opt=='$':
        flag = 0
    else:
        print('Please enter 1 or 2 only')
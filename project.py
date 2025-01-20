import time
import random
import json
import math

json_file1 = open('BP/project/user.json','r')
member = json.load(json_file1)
json_file1.close()

json_file2 = open('BP/project/food.json','r')
food = json.load(json_file2)
json_file2.close()

json_file3 = open('BP/project/offer.json','r')
offer = json.load(json_file3)
json_file3.close()

# member = json.load(json_file1)
# food = json.load(json_file2)
# offer = json.load(json_file3)

# member = {'amir@899':{'type':'admin','pass':'Q4##56bN','fname':'_','lname':'_','email':'_','phone':'_','fav':'_'},
#           'ahmad@sol':{'type':'employee','pass':'23Cf@vcvbm','fname':'Ahmad','lname':'Mosavi','email':'','phone':'','fav':''},
#           'Sia34Mak':{'type':'employee','pass':'3432SM@12','fname':'Siamak','lname':'Ansari','email':'','phone':'','fav':''},
#           'Alireza12CV':{'type':'employee','pass':'2277020CVVG','fname':'Ali','lname':'jamshidi','email':'','phone':'','fav':''},
#           'Amini567':{'type':'customer','pass':'20942XsvH@Z','fname':'Ramin','lname':'Amini','email':'','phone':'','fav':''},
#           'Akbari78887@f':{'type':'customer','pass':'35664FTUn45','fname':'Milad','lname':'Akbari','email':'','phone':'','fav':''},}

# food = {'kabab':400000,'Berenj':100000,'Khoresht':220000,'Ghormesabzi':320000,'Zereshkpolo':270000,
#         'Ghime':300000,'Delester':35000,'Salad':15000,'Noshabe':20000,'Dogh':20000}

# offer = {'QWBv23@#v','sd67Hj#!x','23FCV%n&5'}



def sign():
    command = input('wellcome to elmos resturant...\nplease sign in on system\nif you have\'nt an account sign up\n1.sign in\n2.sign up\n')
    if(command == 'exit'):
        quit()
    elif(command == '1'):
        print('\n')
        signin()
    elif(command == '2'):
        print('\n')
        signup()
    else:
        print('\n')
        sign()

def signin():
    counter = 0
    while(True):
        command = input('please enter your username:\n')
        if(command == 'exit'):
            quit()
        elif(command in list(member.keys())):
            print('\n')
            user = command
            break
        else:
            print('\n')
            counter += 1
            print('username is incorrect')
            if(counter >= 3):
                counter = 0
                print('wait 2 minute...')
                start = time.time()
                while(True):
                    if(time.time() - start > 10):
                        break
            continue
    counter = 0
    while(True):
        command = input('if you forgot the password enter 1\nplease enter your password:\n')
        if(command == 'exit'):
            quit()
        elif(command == '1'):
            print('\n')
            forgot(user)
            break
        elif(command == member[user]['pass']):
            print('\n')
            page(user)
            break
        else:
            print('\n')
            counter += 1
            print('password is incorrect')
            if(counter >= 3):
                counter = 0
                print('wait 2 minute...')
                start = time.time()
                while(True):
                    if(time.time() - start > 10):
                        break
            continue

def forgot(username):
    counter = 0
    while(True):
        command = input('if you forgot the email enter 1\nplease enter your email address:\n')
        if(command == 'exit'):
            quit()
        elif(command == '1'):
            print('\n')
            counter = 0
            while(True):
                command = input('if you want to back enter 1\nplease enter your phone number:\n')
                if(command == 'exit'):
                    quit()
                elif(command == '1'):
                    print('\n')
                    break
                elif(command == member[username]['phone']):
                    print('\n')
                    counter = 0
                    while(True):
                        command = input('if you want to back enter 1\nplease enter your fav food:\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '1'):
                            print('\n')
                            break
                        elif(command == member[username]['fav']):
                            print('\n')
                            page(username)
                            return 0
                        else:
                            print('\n')
                            counter += 1
                            print('fav is incorrect')
                            if(counter >= 3):
                                counter = 0
                                print('wait 2 minute...')
                                start = time.time()
                                while(True):
                                    if(time.time() - start > 10):
                                        break
                        continue
                else:
                    print('\n')
                    counter += 1
                    print('phone is incorrect')
                    if(counter >= 3):
                        counter = 0
                        print('wait 2 minute...')
                        start = time.time()
                        while(True):
                            if(time.time() - start > 10):
                                break
                    continue
        elif(command == member[username]['email']):
            print('\n')
            page(username)
            break
        else:
            print('\n')
            counter += 1
            print('email is incorrect')
            if(counter >= 3):
                counter = 0
                print('wait 2 minute...')
                start = time.time()
                while(True):
                    if(time.time() - start > 10):
                        break
            continue

def signup():

    global member

    while(True):
        fname = input('please enter your first name:\n')
        if(fname == 'exit'):
            quit()
        else:
            print('\n')
            break
    while(True):
        lname = input('please enter your last name:\n')
        if(lname == 'exit'):
            quit()
        else:
            print('\n')
            break
    while(True):
        username = input('please enter your username\n(your username must be unique):\n')
        if(username == 'exit'):
            quit()
        elif(len(username) >= 5):
            if(username in list(member.keys())):
                print('\n')
                print('username takan by someone else')
            else:
                print('\n')
                break
        else:
            print('\n')
            print('username must be more than 5 characters')
            continue
    while(True):
        recomend = str(random.randint(100000,999999)) + 'FN'
        print(f'we recomend you this password...\n({recomend})\nif you want this enter 1')
        password = input('otherwise, enter your password:\n')
        if(password == 'exit'):
            quit()
        elif(password == '1'):
            print('\n')
            password = recomend
            break
        elif(len(password) >= 8):
            print('\n')
            break
        else:
            print('\n')
            print('password must be more than 8 characters')
            continue

    emails = []
    phones = []
    for key in member:
        emails.append(member[key]['email'])
        phones.append(member[key]['phone'])
    
    while(True):
        email = input('please enter your email address\n')
        if(email == 'exit'):
            quit()
        elif(email in emails):
            print('\n')
            print('email must be unique')
            continue
        else:
            print('\n')
            break
    while(True):
        phone = input('please enter your phone number\n')
        if(phone == 'exit'):
            quit()
        elif(phone in phones):
            print('\n')
            print('phone must be unique')
            continue
        else:
            print('\n')
            break
    while(True):
        fav = input('please enter your fav food:\n')
        if(fav == 'exit'):
            quit()
        else:
            print('\n')
            break
    
    member[username] = {'type':'customer','pass':password,'fname':fname,'lname':lname,'email':email,'phone':phone,'fav':fav}
    with open('BP/project/user.json', 'w') as json_file:
        json.dump(member, json_file, indent=3)
    page(username)
    
def page(username):
    print('wellcome ' + member[username]['fname'] + " " + member[username]['lname'])
    while(True):
        if(member[username]['type'] == 'admin'):
            #code
        elif(member[username]['type'] == 'employee'):
            #code
        elif(member[username]['type'] == 'customer'):
            #code

sign()
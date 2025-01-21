import time
import random
import json
import re
import math

json_file1 = open('C://py/BP/project/user.json','r')
member = json.load(json_file1)
json_file1.close()

json_file2 = open('C://py/BP/project/food.json','r')
food = json.load(json_file2)
json_file2.close()

json_file3 = open('C://py/BP/project/offer.json','r')
offer = json.load(json_file3)
json_file3.close()

json_file4 = open('C://py/BP/project/account.json','r')
account = json.load(json_file4)
json_file4.close()
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



def sign(account):
    if(account != ""):
        page(account)
    else:
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
            account['sign'] = user
            with open('C://py/BP/project/account.json','w') as json_file:
                json.dump(account,json_file,indent=3)
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
                        command = input('if you want to back enter 1\nplease enter your favorite food:\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '1'):
                            print('\n')
                            break
                        elif(command == member[username]['fav']):
                            print('\n')
                            account['sign'] = username
                            with open('C://py/BP/project/account.json','w') as json_file:
                                json.dump(account,json_file,indent=3)
                            page(username)
                            return 0
                        else:
                            print('\n')
                            counter += 1
                            print('favorite food is incorrect')
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
            account['sign'] = username
            with open('C://py/BP/project/account.json','w') as json_file:
                json.dump(account,json_file,indent=3)
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
                print('\nusername takan by someone else')
            else:
                print('\n')
                break
        else:
            print('\nusername must be more than 5 characters')
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
            print('\npassword must be more than 8 characters')
            continue

    emails = []
    phones = []
    for key in member:
        emails.append(member[key]['email'])
        phones.append(member[key]['phone'])
    
    while(True):
        email = input('please enter your email address:\n')
        if(email == 'exit'):
            quit()
        elif(email in emails):
            print('\nemail address must be unique')
            continue
        else:
            print('\n')
            break
    while(True):
        phone = input('please enter your phone number:\n')
        if(phone == 'exit'):
            quit()
        elif(phone in phones):
            print('\nphone number must be unique')
            continue
        else:
            print('\nphone number must be unique')
            break
    while(True):
        fav = input('please enter your favorite food:\n')
        if(fav == 'exit'):
            quit()
        else:
            print('\n')
            break
    
    member[username] = {'type':'customer','pass':password,'fname':fname,'lname':lname,'email':email,'phone':phone,'fav':fav,'wallet':'0','cart':[],'payment':'0','history':{}}
    with open('C://py/BP/project/user.json', 'w') as json_file:
        json.dump(member, json_file, indent=3)
    page(username)
    
def page(username):
    print('\n')
    print('wellcome ' + member[username]['fname'] + " " + member[username]['lname'])
    while(True):
        # print('\n')
        if(member[username]['type'] == 'admin'):
            print('\n')
        elif(member[username]['type'] == 'employee'):
             while(True):
                print('\n')
                command = input('1.foods menu\n2.change food price\n3.change employee information\n4.add discount code\n5.customer purchase history\n6.sign out\n')
                if(command == 'exit'):
                    quit()
                elif(command == '1'):
                    print('\n')
                    for key in food:
                        print(key + "..." + str(food[key]))
                elif(command == '2'):
                    while(True):
                        command = input('\nif you want to back enter 0\nenter the name of the desired food:\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '0'):
                            print('\n')
                            break
                        elif(command in list(food.keys())):
                            foodname = command
                            while(True):
                                command = input('\nif you want to back enter 0\nenter the desired amount:\n')
                                pattern = '[0-9]'
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(re.match(pattern,command) and int(command) > 0):
                                    food[foodname] = int(command)
                                    with open('C://py/BP/project/food.json','w') as json_file:
                                        json.dump(food,json_file,indent=3)
                                    print('\nfood price changed successfully')
                                    page(username)
                                else:
                                    print('\nplease enter a valid value')
                                    continue
                        else:
                            print('\nthe desired food is not available')
                            continue
                elif(command == '3'):
                    while(True):
                        command = input('\nif tou want to back enter 0\nselect the information you want to change:\n1.password\n2.email\n3.phone\n4.favorite food\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '0'):
                            print('\n')
                            break
                        elif(command == '1'):
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter the new password:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(len(command) >= 8):
                                    print('\npassword successfully changed')
                                    member[username]['pass'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break
                                else:
                                    print('\npassword must be more than 8 characters')
                                    continue
                        elif(command == '2'):
                            emails = []
                            for key in member:
                                emails.append(member[key]['email'])
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter the new email address:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(command not in emails):
                                    print('\nemail address successfully changed')
                                    member[username]['email'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break
                                else:
                                    print('\nemail address must be unique')
                                    continue
                        elif(command == '3'):
                            phones = []
                            for key in member:
                                phones.append(member[key]['phone'])
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter the new phone number:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(command not in phones):
                                    print('\nphone number successfully changed')
                                    member[username]['phone'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break
                                else:
                                    print('\nphone number must be unique')
                                    continue
                        elif(command == '4'):
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter your fav food:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                else:
                                    print('\nfavorite food successfully changed')
                                    member[username]['fav'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break      
                        else:
                            print('\nPlease select from the options')
                            continue
                elif(command == '4'):
                    command = input('\nif you want to back enter 0\nplease enter the new discount code:\n')
                    if(command == 'exit'):
                        quit()
                    elif(command == '0'):
                        print('\n')
                        break
                    elif(command not in list(offer.keys())):
                        offer[command] = command
                        with open('C://py/BP/project/offer.json','w') as json_file:
                            json.dump(offer,json_file,indent=3)
                        print('\ndiscount code successfully added')
                        break
                    else:
                        print('\ndiscount code already exists')
                        continue
                elif(command == '5'):
                    while(True):
                        command = input('\nif you want to back enter 0\nplease enter your username:\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '0'):
                            print('\n')
                            break
                        elif(command in list(member.keys())):
                            print('\n')
                            for key in member[command]['history']:
                                print("\n" + key + ":")
                                sum = 0
                                for item in member[command]['history'][key]:
                                    print(item[0] +"..."+ str(item[1]))
                                    sum += item[1]
                                print(f'total price: {sum}')
                            break
                        else:
                            print('\nusername is incorrect')
                            continue
                elif(command == '6'):
                    print('\n')
                    account['sign'] = ""
                    with open('C://py/BP/project/account.json','w') as json_file:
                        json.dump(account,json_file,indent=3)
                    sign(account['sign'])
                else:
                    print('\nplease select from the option')
                    continue
        elif(member[username]['type'] == 'customer'):
            while(True):
                print('\n')
                command = input('1.foods menu\n2.add or remove foods from shopping cart\n3.purchase and payment\n4.change customer information\n5.recharge wallet\n6.previous purchases\n7.sign out\n')
                if(command == 'exit'):
                    quit()
                elif(command == '1'):
                    print('\n')
                    for key in food:
                        print(key + "..." + str(food[key]))
                elif(command == '2'):
                    while(True):
                        print('\n')
                        print('if you want to back enter 0')
                        command = input('1.view shopping cart\n2.add food\n3.remove food\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '0'):
                            print('\n')
                            break
                        elif(command == '1'):
                            print('\n')
                            if(len(member[username]['cart']) == 0):
                                print('shopping cart is empty')
                            else:
                                sum = 0
                                for key in member[username]['cart']:
                                    print(key[0] +"..."+ str(key[1]))
                                    sum += key[1]
                                print(f'total price: {sum}')
                        elif(command == '2'):
                            print('\n')
                            while(True):
                                command = input('if you want to back enter 0\nplease enter the desired food to add to cart:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(command in list(food.keys())):
                                    print('\n')
                                    print('food added to cart')
                                    order = []
                                    order.append(command)
                                    order.append(food[command])
                                    member[username]['cart'].append(order)
                                    with open('C://py/BP/project/user.json','w') as json_file3:
                                        json.dump(member,json_file3,indent=3)
                                else:
                                    print('\n')
                                    print('Please enter the correct name of the food.')
                                    continue
                        elif(command == '3'):
                             print('\n')
                             while(True):
                                command = input('if you want to back enter 0\nplease enter the desired food to remove from cart:\n')
                                order = []
                                if(command in list(food.keys())):
                                    order.append(command)
                                    order.append(food[command])
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(order in member[username]['cart']):
                                    print('\n')
                                    print('food removed from cart')
                                    # order = []
                                    # order.append(command)
                                    # order.append(food[command])
                                    member[username]['cart'].remove(order)
                                    with open('C://py/BP/project/user.json','w') as json_file3:
                                        json.dump(member,json_file3,indent=3)
                                else:
                                    print('\n')
                                    print('Please enter the correct name of the food.')
                                    continue
                        else:
                            print('\n')
                            continue
                elif(command == '3'):
                    discount = False
                    discode = ''
                    while(True):
                        print('\n')
                        sum = 0
                        for key in member[username]['cart']:
                            print(key[0] +"..."+ str(key[1]))
                            sum += key[1]
                        print(f'total price: {sum}')
                        if(int(member[username]['payment']) >= 250000):
                            print('\n20% discount')
                            sum *= 0.8
                            sum = math.floor(sum)
                        else:
                            print('\nthere is no shopping rewards')
                        if(discount):
                            print('50% discount')
                            sum *= 0.5
                            sum = math.floor(sum)
                        else:
                            print('there is no discount')
                        print(f'total price after discount: {sum}\n')
                        command = input('if you want to back enter 0\n1.enter discount code\n2.payment\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '0'):
                            print('\n')
                            break
                        elif(command == '1'):
                            print('\n')
                            while(True):
                                command = input('if you want to back enter 0\nenter your discount code:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(command in list(offer.keys())):
                                    print('\ndiscount code applied')
                                    discount = True
                                    discode = command
                                    break
                                else:
                                    print('\ndiscount code is incorrect')
                                    continue
                        elif(command == '2'):
                            print('\n')
                            # if(discount):
                            #     offer.pop(discode)
                            #     with open('C://py/BP/project/offer.json','w') as json_file:
                            #         json.dump(offer,json_file,indent=3)
                            if(sum <= int(member[username]['wallet'])):
                                history = member[username]['history']
                                history[str(len(history) + 1)] = member[username]['cart'].copy()
                                member[username]['wallet'] = str(int(member[username]['wallet']) - sum)
                                member[username]['payment'] = str(sum)
                                member[username]['cart'].clear()
                                with open('C://py/BP/project/user.json','w') as json_file:
                                    json.dump(member,json_file,indent=3)
                                print('your purchase was successful')
                                break
                            else:
                                print('\ninsufficient wallet balance\nplease charge your wallet or remove food from cart')
                                continue
                        else:
                            print('\n')
                            continue
                elif(command == '4'):
                    print('\n')
                    while(True):
                        command = input('if tou want to back enter 0\nselect the information you want to change:\n1.password\n2.email\n3.phone\n4.favorite food\n')
                        if(command == 'exit'):
                            quit()
                        elif(command == '0'):
                            print('\n')
                            break
                        elif(command == '1'):
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter the new password:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(len(command) >= 8):
                                    print('\npassword successfully changed')
                                    member[username]['pass'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break
                                else:
                                    print('\npassword must be more than 8 characters')
                                    continue
                        elif(command == '2'):
                            emails = []
                            for key in member:
                                emails.append(member[key]['email'])
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter the new email address:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(command not in emails):
                                    print('\nemail address successfully changed')
                                    member[username]['email'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break
                                else:
                                    print('\nemail address must be unique')
                                    continue
                        elif(command == '3'):
                            phones = []
                            for key in member:
                                phones.append(member[key]['phone'])
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter the new phone number:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                elif(command not in phones):
                                    print('\nphone number successfully changed')
                                    member[username]['phone'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break
                                else:
                                    print('\nphone number must be unique')
                                    continue
                        elif(command == '4'):
                            while(True):
                                command = input('\nif you want to back enter 0\nplease enter your fav food:\n')
                                if(command == 'exit'):
                                    quit()
                                elif(command == '0'):
                                    print('\n')
                                    break
                                else:
                                    print('\nfavorite food successfully changed')
                                    member[username]['fav'] = command
                                    with open('C://py/BP/project/user.json','w') as json_file:
                                        json.dump(member,json_file,indent=3)
                                    break      
                        else:
                            print('\nPlease select from the options')
                            continue
                elif(command == '5'):
                    while(True):
                        command = input('if you want to back enter 0\nPlease enter the desired amount:\n')
                        pattern = '[0-9]'
                        if(command == 'exit'):
                            quit()
                        elif(command == '0'):
                            print('\n')
                            break
                        elif(re.match(pattern,command) and int(command) > 0):
                            print('\n')
                            print('wallet successfully charged')
                            wallet = int(member[username]['wallet']) + int(command)
                            member[username]['wallet'] = str(wallet)
                            with open('C://py/BP/project/user.json', 'w') as json_file:
                                json.dump(member, json_file, indent=3)
                            break
                        else:
                            print('\n')
                            print('please enter a valid value')
                            continue
                elif(command == '6'):
                    print('\n')
                    for key in member[username]['history']:
                        print("\n" + key + ":")
                        sum = 0
                        for item in member[username]['history'][key]:
                            print(item[0] +"..."+ str(item[1]))
                            sum += item[1]
                        print(f'total price: {sum}')
                elif(command == '7'):
                    print('\n')
                    account['sign'] = ""
                    with open('C://py/BP/project/account.json','w') as json_file:
                        json.dump(account,json_file,indent=3)
                    sign(account['sign'])
                else:
                    print('\nplease select from the option')
                    continue

sign(account['sign'])
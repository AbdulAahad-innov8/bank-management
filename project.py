import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")        
    except Exception as err:
        print(f"an exception has occurred as {err}")

    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))     


    def Createaccount(self):
        info = {
            "name": input("please enter your name-"),
            "age": int(input("please enter your age-")),
            "pin": int(input("please enter the 4 digit pin")),
            "accountno.": 12345,
            "balance": 0
        } 

        if  info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("your account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)
            Bank.update() 


    def depositmoney(self):
        accnumber = int(input("please tell your accnumber"))
        pin = int(input("please tell your pin as well"))
        userdata = [i for i in Bank.data if i['accountno.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")

        else:
            amount = int(input("how much amount you want to deposit"))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.update()
                print("amount deposited successfully")


    def withdrawmoney(self):
        accnumber = int(input("please tell your accnumber"))
        pin = int(input("please tell your pin as well"))
        userdata = [i for i in Bank.data if i['accountno.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("sorry no data found")
        
        else:
            amount = int(input("how much amount you want to withdraw"))
            if userdata [0]['balance'] < 0:
                print("sorry you dont have that much money")
            else:
                print(userdata)
                userdata[0]['balance'] -= amount
                Bank.update()
                print("amount withdrawn successfully")


    def showdetails(self):
        accnumber = int(input("please tell your accnumber"))
        pin = int(input("please tell your pin as well"))
        userdata = [i for i in Bank.data if i['accountno.'] == accnumber and i['pin'] == pin]
        print("your information are/n/n/n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnumber = int(input("please tell your accnumber"))
        pin = int(input("please tell your pin as well"))
        userdata = [i for i in Bank.data if i['accountno.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found")

        else:
            print("you cannot change the age, account number, balance")

            print("fill the details for change or leave it empty if no change")   
            newdata = {
                "name" : input("please tell the new name or press enter:"),
                "pin": input("please enter the new pin or press enter to skip")
                } 

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']   

            newdata['age'] = userdata[0]['age']

            newdata['accountno.']  = userdata[0]['accountno.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] =int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.update()
            print("datails updated successfully") 

    def delete(self):
        accnumber = int(input("please tell your accnumber"))
        pin = int(input("please tell your pin as well"))
        userdata = [i for i in Bank.data if i['accountno.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such data exist")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == 'N':
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully")
                Bank.update()    







                      




user = Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the amount") 
print("press 4 for showing the details")
print("press 5 for updating the detials")
print("press 6 for deleting the account")
check = int(input("tell your response-"))      
if check == 1:
    user.Createaccount()
if check == 2:
    user.depositmoney()         
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.delete()    

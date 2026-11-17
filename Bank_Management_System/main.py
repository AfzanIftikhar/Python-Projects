import random
import json
import string
from pathlib import Path

class Bank():
    database = 'data.json'
    data = []


    try:
        if Path(database).exists:
            with open(database) as file:
                data = json.loads(file.read())
           
        else:
            print("No such File Exist")


    except Exception as err:
        print(f"An exception occured as {Exception}")        

    @classmethod
    def __update(cls):
        with open(cls.database,"w") as file:
            file.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits,k=3)
        special = random.choices("@!#$%^&*",k=1)
        id = alpha + num + special
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name" : input("Enter your name : "),
            "age" :int(input("Enter your age : ")),
            "email" : input("Enter your Email : "),
            "accountNo.": Bank.__accountGenerate(),
            "pin" :int(input("Enter 4 digit pin : ")),
            "balance" : 0

        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry your account cannot be created")
        else:
            print("----------------------------------------------")
            print("Account Created Successfully ! ")    
            for i in info:
                print(f"{i} : {info[i]}")

            print("----------------------------------------------")    
            print("please note down your account number")
    
            Bank.data.append(info)
            Bank.__update()


    def depositmoney(self):
        accno = input("Please enter your account number : ")
        pin = int(input("please enter your pin : "))
       
        userdata = [i for i in Bank.data if i["accountNo."] == accno and i["pin"] == pin]
       
        if userdata == False:
            print("Sorry no such User found !")
        else:
            amount = int(input("Please enter the amount you want to deposit : "))
            if amount > 10000 or amount <= 0:
                print("Sorry the amount should be greater then 0 nad lower then 10000")
            else:
                userdata[0]['balance'] += amount
                print("Amount deposited successfully !")
                Bank.__update()

    def withdraw(self):
        accno = input("Please enter your account number : ")
        pin = int(input("please enter your pin : "))
               
        userdata = [i for i in Bank.data if i["accountNo."] == accno and i["pin"] == pin]
               
        if userdata == False:
            print("Sorry no such User found !")
        else:
            amount = int(input("Please enter the amount you want to withdraw : "))
            if userdata[0]['balance'] < amount:
                print("Sorry you don' have that much money")
            elif amount < 500 or amount % 500 != 0:
                print("The amount should be greater or equal to 500 and should be multiple of 500")
            else:
                userdata[0]['balance'] -= amount
                print("Amount withdrawn successfully !")
                Bank.__update()

    def show_details(self):
        accno = input("Please enter your account number : ")
        pin = int(input("please enter your pin : "))
               
        userdata = [i for i in Bank.data if i["accountNo."] == accno and i["pin"] == pin]
        print("==========================================")
        print("--------------Your Details----------------")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
        print("==========================================")

    def update_details(self):
        accno = input("Please enter your account number : ")
        pin = int(input("please enter your pin : "))
                       
        userdata = [i for i in Bank.data if i["accountNo."] == accno and i["pin"] == pin]
        if userdata == False:
            print("Sorry no such data available")

        else:

            print("You can update your name,email and pin only ! ")

            print("Fill the following details or just leave it as it is ! ")    
            newData = {
                "name" :input("Enter new name or press enter to skip : ") ,
                "email": input("Enter new email or press enter to skip : "),
                "pin": int(input("Enter new pin or press enter to skip : "))
            }

            if newData["name"] == "":
                newData["name"] = userdata[0]["name"]
            if newData["email"] == "":
                newData["email"] = userdata[0]["email"]
            if newData["pin"] == "":
                newData["pin"] = userdata[0]["pin"]

            print(userdata)
            newData["accountNo."] = userdata[0]["accountNo."]
            newData["age"] = userdata[0]["age"]
            newData["balance"] = userdata[0]["balance"]

            if type(newData["pin"]) == str:
                newData["pin"] = int(newData["pin"])

            for i in newData:
                if newData[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] == newData[i]

            Bank.__update()    
            print("Details updated succesfully !")


    def Delete(self):
        accno = input("Please enter your account number : ")
        pin = int(input("please enter your pin : "))
                               
        userdata = [i for i in Bank.data if i["accountNo."] == accno and i["pin"] == pin]
        if userdata == False:
            print("Sorry no such data available")
        else:
            index = Bank.data.index(userdata[0])
            Bank.data.pop(index)
            Bank.__update()
            print("Account Deleted Successfully !")
        
            

user = Bank()
print("====================================================")
print("Press 1 for creating an account")
print("Press 2 for deposting an amount")
print("Press 3 to withdraw an amount")
print("Press 4 to see details")
print("Press 5 to update details ")
print("Press 6 to delete account ")

print("====================================================")
check = int(input("Please enter your number : "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdraw()

if check == 4:
    user.show_details()    


if check == 5:
    user.update_details()


if check == 6:
    user.Delete()
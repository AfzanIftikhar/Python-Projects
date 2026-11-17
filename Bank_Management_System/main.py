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
            "pin" :input("Enter 4 digit pin : "),
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
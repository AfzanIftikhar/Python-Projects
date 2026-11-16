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
    def create_account(self):
        pass


user = Bank()
print("====================================================")
print("Press 1 for creating an account")
print("Press 2 for deposting an amount")
print("Press 3 to withdraw an amount")
print("Press 4 to see details")
print("Press 5 to update details ")
print("Press 6 to delete account ")

print("====================================================")
check = input("Please enter your number : ")

if check == 1 :
    user.create_account()
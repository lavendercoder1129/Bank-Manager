import json
from pathlib import Path

class Bank:

    database = 'data.json'
    data = []

    try : 
        if Path(database).exists(): 
            with open(database) as fs :
                data = json.loads(fs.read())
        else :
            print("File does not exists")
    except Exception as err :
        print(f"An unexpected error occured as {err}")






    def createaccount(self):
        pass

print("Press 1 to create Account")
print("Press 2 to Deposit Money in account")
print("Press 3 to Withdraw Money from account")
print("Press 4 to view Account details")
print("Press 5 to update account details")
print("Press 6 to delete account")


check = int(input("Enter your choice"))

if check == 1 : 
    Bank.createaccount()
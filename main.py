import json
import random
import string
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

    @classmethod
    def __update(cls):
        with open(cls.database,"w") as fs :
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=4)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id) 

    def createaccount(self):
        info = {
            "name" : input("Enter your full name :- "),
            "age" : int(input("Enter your age :- ")),
            "email" : input("Enter your email address :- "),
            "pin" : int(input("Enter your 4 digit pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }

        if info['age'] < 18 :
            print("Sorry you are underaged to create an account")
        elif len(str(info['pin'])) != 4 : 
            print("Enter a 4 digit pin only")
        else : 
            print("Account created successfully")
            for i in info : 
                print(f"{i} : {info[i]}")
            print("Please note down your Account Number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self) : 
        accnumber = input("Please Enter your Account Number : ")
        pin = int(input("Please enter your PIN : "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False : 
            print("Data not found. Try again")
        else : 
            amount = int(input("Enter amount to Depoit :- "))
            if amount > 100000 or amount < 0 : 
                print("You can only deposit amount between 0 and 10,000")
            else : 
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amout Deposited Succesfully")

print("Press 1 to create Account")
print("Press 2 to Deposit Money in account")
print("Press 3 to Withdraw Money from account")
print("Press 4 to view Account details")
print("Press 5 to update account details")
print("Press 6 to delete account")


check = int(input("Enter your choice"))

if check == 1 : 
    Bank.createaccount()
elif check == 2 : 
    Bank.depositmoney()
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
    
    def withdrawmoney(self) :
        accnumber = input("Enter your account number :- ")
        pin = int(input("Please enter your PIN :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin ]

        if userdata == False : 
            print("No data found")
        else : 
            amount = int(input("Enter amount to withdraw :- "))
            if userdata[0]['balance'] < amount :
                print("Insufficient funds")
            else : 
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrawn successfully")

    def showdetails(self):
        accnumber = input("Enter your account number :- ")
        pin = int(input("Please enter your PIN :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin ]

        print("\nYour infoformation : \n")
        for i in userdata[0] :
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self) : 
        accnumber = input("Enter your account number :- ")
        pin = int(input("Please enter your PIN :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin ]
        
        if userdata == False : 
            print("Invalid Data") 
        else : 
            print("You cannot edit age, account number and balance")
            print("Enter details to update name, email, pin or leave empty if no change")

            newdata= {
                "name" : input("Enter your new name or Enter to skip :- "),
                "email" : input("Enter your new email or Enter to skip :- "),
                "pin" : input("Enter new Pin or Enter to skip :- ")
            }

            if newdata['name'] == "" :
                newdata['name'] = userdata[0]['name']
            if newdata['email'] == "" :
                newdata['email'] = userdata[0]['email']
            if newdata['pin'] == "" :
                newdata['pin'] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str : 
                newdata['pin'] = int(newdata['pin'])
            
            for i in newdata : 
                if newdata[i] == userdata[0][i] :
                    continue
                else : 
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Account information updated Successfully")


user = Bank()
print("Press 1 to create Account")
print("Press 2 to Deposit Money in account")
print("Press 3 to Withdraw Money from account")
print("Press 4 to view Account details")
print("Press 5 to update account details")
print("Press 6 to delete account")


check = int(input("Enter your choice"))

if check == 1 : 
    user.createaccount()
elif check == 2 : 
    user.depositmoney()
elif check == 3 : 
    user.withdrawmoney()
elif check == 4 : 
    user.showdetails()
elif check == 5 : 
    user.updatedetails()
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

        if not userdata : 
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

        if not userdata : 
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

        print("\nYour information : \n")
        for i in userdata[0] :
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self) : 
        accnumber = input("Enter your account number :- ")
        pin = int(input("Please enter your PIN :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin ]
        
        if not userdata : 
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

    def deleteaccount(self) : 
        accnumber = input("Enter your account number :- ")
        pin = int(input("Enter your PIN :- "))
        userdata = [i for i in Bank.data if i['accoountNo.'] == accnumber and i['pin'] == pin]

        if not userdata :
            print("Invalid data")
        else :
            check = input("Press Y to confirm delete account else press n")
            if check == 'n' or check == 'N':
                print("Deletion cancelled")
            else : 
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update() 
    
    def transfermoney(self):
        sender_accno = input("Enter your account nummber :- ")
        sender_pin = int(input("Enter your PIN :- "))

        senderdata = [i for i in Bank.data if i['accountNo.'] == sender_accno and i['pin'] == sender_pin]

        if not senderdata :
            print("Invalid sender details")
        else :
            receiver_accno = input("Enter reciever account Number :- ")
            receiverdata = [i for i in Bank.data if i['accountNo.'] == receiver_accno]

            if not receiverdata : 
                print("Invalid receiver details")
            else : 
                amount = int(input("Enter amount to transfer :- "))

                if amount <= 0 : print("Invalid amount")
                elif senderdata[0]['balance'] < amount:
                    print("Insufficient balance")
                else : 
                    senderdata[0]['balance'] -= amount
                    receiverdata[0]['balance'] += amount
                    Bank.__update()
                    print("Amount transferred successfully.") 

user = Bank()
print("Press 1 to Create a new Account.")
print("Press 2 to Deposit Money in Account.")
print("Press 3 to Withdraw Money from Account.")
print("Press 4 to view Account details.")
print("Press 5 to update Account details.")
print("Press 6 to delete A1ccount.")
print("Press 7 to transfer money")


check = int(input("Enter your choice :- "))

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
elif check == 6 : 
    user.deleteaccount()
elif check == 7 :
    user.transfermoney()
else : print("Invalid choice")
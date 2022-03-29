#Banking App


accountNo = " "
CusName = " "
BCode = " "
Mobile = 0
Bal = 0

#f = open("bankfile", "r")

#accountNo = " "
#CusName = " "
#BCode = " "
#Mobile = 0
#Bal = 0

#f.read()
#f.close()

def CreateAnAcc():
    accountNo = int(input("enter account Number:\n"))
    CusName = input("enter Name:\n")
    BCode = input("enter Branch Code:\n")
    Mobile = int(input("enter Mobile Number:\n"))
    Bal = int(input("enter current Balance:\n"))

def ShowAccDetails():
    print("AccountNO:",accountNo)
    print("customerName:",CusName)
    print("Bcode",BCode)
    print("mobile:",Mobile) 

def Deposit(amount) :
    Bal = " "+ amount
    checkbalance()

def Withdraw(amount) :
    Bal = " " - amount
    checkbalance()

def checkbalance(Balance) :
    Bal=Balance
    print("current Balance:",Bal)

#MAIN
ch1='y'
while(ch1=='y') :
    print("""
    1.Would you like to make a transaction?
    2.Would you like to make a deposit or withdrawal?
    3.How much would you like to deposit OR How much would you like to withdraw?
    Current balance
    """)
    channel=int(input("Select any option:\n"))

    if(channel==1) : 
        CreateAnAcc()

    elif(channel==2):
            choice=(input("Do you want to deposit or withdraw:\nSelect 'y' for deposit and 'n' for withdrawal\n"))

            if choice == 'yes':
                print(int(input("Enter your account number for a deposit:\n")))
            elif choice == 'no':
                print(int(input("Enter your account number for a withdrawal:\n")))

    elif (channel==3) :
            amount=int(input("Enter amount to Deposit:\n"))
            Deposit('amount')

    elif (channel==4) :
        checkbalance()

    elif (channel==5):
        print("Goodbye")
        break

    else:
        print("please select any 4 options available above ")
        print("do you want to continue...press y.")
        channel1=input()
        
'''Project Name : Banking Management System.
Author : Shaily Kesharwani
Date : 27/02/2023
Language : Python 3.10.6
Details : This helps us to enter, display or alter the details of different accounts in the bank.
Version : 1.0.5'''




import os
#os - allow us to run a command in the python script 
import platform
# platform - provides functions that access information of the underlying platform
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host="localhost",
                               user="shaily08",
                               password="shailyk7981",
                               database="bank")
mycursor = mydb.cursor()

print("\n****welcome To The Banking Management****")
print("Here You Can ..ADD CUSTOMER.. , ..DEPOSIT MONEY.. And So On....\n")


def AccInsert():
    List=[]
    account_no = int(input("Enter the Account number : "))
    List.append(account_no)
    name = input("Enter the Customer Name: ")
    List.append(name)
    age = int(input("Enter Age of Customer : "))
    List.append(age)
    occupation = input("Enter the Customer Occupation : ")
    List.append(occupation)
    address = input("Enter the Address of the Customer : ")
    List.append(address)
    mobile = int(input("Enter the Mobile number : "))
    List.append(mobile)
    aadhaar_no = int(input("Enter the Aadhaar number : "))
    List.append(aadhaar_no)
    Amt = float(input("Enter the Money Deposited : "))
    List.append(Amt)
    acc_type = input("Enter the Account Type (Saving/RD/PPF/Current) : ")
    List.append(acc_type)
    customer= (List)
    sql = '''INSERT INTO desc_account(account_no, name, age, occupation, address, mobile, aadhaar_no, amt, acc_type) values(%s,%s,%s, %s,%s,%s, %s,%s,%s)'''
    mycursor.execute(sql, customer)
    mydb.commit()
    print("\nYou have Successfully Added the Customer")


def AccView():
    set = input("Enter the ACC no whom you want to see: ")
    var = (set)
    sql = "SELECT * FROM desc_account WHERE account_no=" + set
    mycursor.execute(sql, var)
    my_var = mycursor.fetchall()
    print("The Customer details are as follows : \n")
    data = pd.DataFrame(my_var, columns=['id',  'acc_no',  'name',  'age',  'occupation',  'address',   'mobile',  'aadhaar_no',  'amt',  'acc_type'])
    print(data)


def AccDeposit():
    List = []
    acc_no = int(input("Enter the Account number : "))
    List.append(acc_no)
    amountdeposite = eval(input("Enter the Amount to be deposited : "))
    List.append(amountdeposite)
    month = input("Enter month of Salary : ")
    List.append(month)
    customer = (List)
    sql = "Insert into desc_amt (acc_no, amountdeposite, month) values(%s,%s,%s)"
    mycursor.execute(sql, customer)
    mydb.commit()
    print("Your Money has deposited Sucessfully!")


def accView():
    Accno = input("Enter the Account number of the Customer whose amount is to be viewed : ")

    sql = '''Select desc_account.account_no, desc_account.name, desc_account.age,desc_account.occupation,desc_account.address,desc_account.mobile,desc_account.aadhaar_no,desc_account.amt,desc_account.acc_type, sum(desc_amt.amountdeposite),
    desc_amt.month from desc_account INNER JOIN desc_amt ON desc_account.account_no = desc_amt.acc_no and desc_amt.acc_no =''' + Accno
    var= (Accno)
    mycursor.execute(sql, var)
    my_var = mycursor.fetchall()
    for x in my_var:
        print(x)


def closeAcc():
    Accno =input("Enter the Account number of the Customer to be closed : ")
    var = (Accno)
    sql = "DELETE FROM desc_account WHERE account_no =" + Accno
    mycursor.execute(sql, var)
    sql = "DELETE FROM desc_amt WHERE acc_no=" + Accno
    mycursor.execute(sql, var)
    mydb.commit()
    print("**Your account has closed! Revisit Again**")


def MenuSet():
    print("Enter 1 : To Add Customer")
    print("Enter 2 : To View Customer ")
    print("Enter 3 : To Deposit Money ")
    print("Enter 4 : To Close Account")
    print("Enter 5 : To View All Customer Details")
    try:
        userInput = int(input("\nPlease Choose One Of An Above Option: "))
    except ValueError:
        exit("\nHy! That's Not A Number")
    else:
        print("\n")
        if (userInput == 1):
            AccInsert()
        elif (userInput == 2):
            AccView()
        elif (userInput == 3):
            AccDeposit()
        elif (userInput == 4):
            closeAcc()
        elif (userInput == 5):
            accView()
        else:
            print("Enter correct choice. . . ")
MenuSet()


def runAgain():
    runAgn = input("\nwant To Run Again Y/n: ")
    while (runAgn.lower() == 'y'):
        if (platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
runAgain()




'''I have used XAMPP server to run mysql database in which i have created 2 table

1. TABLE NAME : desc account
.............................................................
[field       .   type      .  NUll   .    key     .   default 

account_no   . int(15)     .   no    .    primary .    Null
name         . varchar(15) .   no    .            .    Null
age          . int(5)      .   no    .            .    Null
occupation   . varchar(15) .   no    .            .    Null
address      . varchar(50) .   no    .            .    Null
mobile       . int(11)     .   no    .            .    Null
aadhaar_no   . int(16)     .   no    .            .    Null
amt          . double(20,5).   no    .            .    Null
account_type .varchar(15)  .   no    .            .    Null]
.............................................................


2. TABLE NAME : desc amt
.................................................................
[field         . type          .  NUll   .    key     .   default
.
acc_no         .   int(15)     .   yes    .           .       Null
amountdeposite .   double(20,5).   yes    .           .       Null
month          .   varchar(15) .   no     .           .       Null
...................................................................
'''
import csv
from random import randint

file = open("customer.txt", "w")
file.close()
file = open("staff.txt", "w")
file.write("sparklynjewel,dolphin45,kiah2002@gmail.com,Annaliese Ronke")
file.write("\ntallest,kissus,temmy@gmail.com,Maggie Bailey")
file.close()

menu = True

while True:
    menu = int(input("would you like to login or close the app, \nEnter 1 to login and 2 to close the app: \n"))
    if menu == 1:
        print("You have chosen to login")
        break
    if menu == 2:
        print("you have chosen to close the app")
        break
    elif menu != 1 and menu != 2:
        print("invalid input")


def account_details():
    pass


while menu == 1:

    def main():
        with open("staff.txt", "r") as file:
            file_reader = csv.reader(file)
            user_find(file_reader)
            file.close()


    def user_find(file):
        user = input("enter your username\n")
        for row in file:
            if row[0] == user:
                print("username found", user)
                user_found = [row[0], row[1]]
                pass_check(user_found)
                break
            else:
                print("try again")


    def pass_check(user_found):
        user = input("enter your password\n")
        if user_found[1] == user:
            print("password match")
        else:
            print("password not match")


    main()
    print(
        "welcome to the system, please create a new account, check account details, carry out banking transactions or "
        "log out.")
    print("Options: \nCreate a new bank account \nCheck account details \nBank transactions \nLog out")


    class BankAccount:
        def __init__(self, name, balance, account_type, email):
            self.name = name
            self.balance = balance
            self.account_type = account_type
            self.email = email

        def get_data(self, name, balance, account_type, email):
            self.name = name
            self.balance = balance
            self.account_type = account_type
            self.email = email

        def put_data(self):
            print(self.name)
            print(self.balance)
            print(self.account_type)
            print(self.email)


    class Banking:
        def __init__(self):
            self.balance = 0

        def deposit(self):
            amount = float(input("enter amount to be deposited \n"))
            self.balance += amount
            return f"this is the amount deposited %s : %amount "

        def withdraw(self):
            amount = float(input("enter the amount to be withdrawn : "))
            if self.balance >= amount:
                self.balance -= amount
                return f"\n You withdrew : {amount}"
            else:
                return "Insufficient balance"

        def banking_options(self):
            selected_option = (int(input("enter 1 for deposit or 2 for withdrawal \n")))
            if selected_option == 1:
                self.deposit()

            elif selected_option == 2:
                self.withdraw()
                pass
            else:
                print("Enter a valid option")


    while True:
        option = (input("> "))
        if option == "Create a new bank account":
            cus1 = BankAccount("", "", "", "")
            name = (input("Enter name\n"))
            balance = (input("Enter opening balance\n"))
            account_type = (input("Enter type of account, Savings/Current\n"))
            email = (input("Enter email\n"))
            cus1.get_data(name, balance, account_type, email)
            cus1.put_data()
            n = 10
            account_number = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
            print(("this is your account number:" + account_number))
            break
        elif option == "Bank transactions":
            Bank_transactions = Banking()
            print(Bank_transactions.banking_options())
        elif option == "Check account details":
            if account_number == input("Enter account number"):
                A = open("customer.txt")
                A.read()
        elif option == "Log out":
            break
        else:
            print("login page")

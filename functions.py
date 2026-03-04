# Bank System Functions Created by: Felipe Tlusty

# This module contains functions for creating accounts, logging in, depositing,
# withdrawing, transferring funds, and printing the menu for the Bank System application.

# Each function interacts with the database to perform the necessary operations and
# returns appropriate values based on the success or failure of the operations.

# Creates a new account with the provided information and an optional initial balance
def create_account(first, last, email, username, password, database, tableName, balance=0):
    database.insertData(tableName=tableName, first=first, last=last, email=email, username=username, password=password, balance=balance)

# Logs in a user by checking the provided username and password against the database
def login(username, password, database, tableName):
    account = database.fetchData(tableName, {"username": username})
    if account:
        print(account[0][5])  # Print the password field of the fetched account
        if account[0][5] == password:
            return True
    return False

# Deposit a specified amount into the user's account if the balance is valid
def deposit(id, amount, balance, database, tableName):
    if balance is not None:
        balance += amount
        database.modifyData(tableName, {"id": id}, {"balance": balance})
        return True
    return False
    
# Withdraw a specified amount from the user's account if the balance is sufficient
def withdraw(id, amount, balance, database, tableName):
    if balance is not None and balance >= amount:
        balance -= amount
        database.modifyData(tableName, {"id": id}, {"balance": balance})
        return amount
    return False

# Transfer a specified amount from the sender's account to the recipient's account if the sender has sufficient balance
def transfer(sender_id, recipient_id, amount, balance, database, tableName):
    if balance is not None and balance >= amount:
        recipient_balance = int(database.fetchEntry(tableName, {"id": recipient_id}, "balance"))
        if recipient_balance is not None:
            balance -= amount
            database.modifyData(tableName, {"id": sender_id}, {"balance": balance})
            recipient_balance += amount
            database.modifyData(tableName, {"id": recipient_id}, {"balance": recipient_balance})
            return True
    return False

# Print the main menu with options based on the user's login status and current balance
def printMenu(loggedIn, username, balance):
    print("#===========================================#")
    if loggedIn:
        print("#           Welcome to the Bank!            #")
        print("#                                           #")
        print("#           Logged in as: {:<18}#".format(username))
        print("#           Current Balance: ${:<14}#".format(balance))
    print("#                                           #")
    print("#           Choose Your Action:             #")
    if not loggedIn:
        print("#           1. Create Account               #")
        print("#           2. Login                        #")
    if loggedIn:
        print("#           3. Deposit                      #")
        print("#           4. Withdraw                     #")
        print("#           5. Transfer                     #")
        print("#           6. Logout                       #")
        print("#           7. Close Account                #")
    print("#           8. Exit                         #")
    print("#           9. Print                        #")
    print("#                                           #")
    print("#===========================================#")
    

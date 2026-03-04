# Bank System Main Application Created by: Felipe Tlusty
# This is the main application file for the Bank System. It initializes the database, creates necessary tables,
# and provides a command-line interface for users to interact with the system. Users can create accounts, log in,
# deposit funds, withdraw funds, transfer funds, and view their account information. The application uses
# functions defined in the functions.py module to perform these operations and interacts with the database through
# the Database class defined in the database.py module. The application also includes error handling and input
# validation to ensure a smooth user experience. The main loop of the application continues until the user chooses
# to exit, allowing for multiple operations to be performed in a single session.


from functions import *
from database import Database
import re
import random

# Sample user data for testing
users = [["john", "doe", "jdoe@gmail.com", "jdoe", "password123", 1000],
         ["jane", "doe", "janedoe@gmail.com", "janedoe", "password321", 2000],
         ["bob", "smith", "bsmith@gmail.com", "bsmith", "password213", 100],
         ["alice", "smith", "asmith@gmail.com", "asmith", "password312", 10000],
         ["charlie", "brown", "charliebrownjr@gmail.com", "cbrown", "password231", 3726],
         ["lucy", "brown", "lbrown@gmail.com", "lbrown", "password132", 4828],
         ["snoopy", "brown", "snoopdawg@gmail.com", "snoopy", "password321", 1928],
         ["linus", "brown", "linustechtips@gmail.com", "linus", "password213", 402984],
         ["sally", "brown", "sally@gmail.com", "sally", "password123", 3882],
         ["peppermint", "patty", "pp@gmail.com", "ppatty", "password321", 102938]]


if __name__ == "__main__":
    # Database Variables
    dbName = "bank_system"
    serverName = "localhost"
    username = "root"
    password = "fracote3"

    # Initialize the database and create necessary tables
    newDB = Database(dbName, serverName, username, password)
    newDB.createTable("users", id="INT PRIMARY KEY AUTO_INCREMENT",
                    first="VARCHAR(15)", last="VARCHAR(15)", email="VARCHAR(30)", username="VARCHAR(15) UNIQUE", password="VARCHAR(15)", balance="INT")
    newDB.createTable("transactions", id="INT PRIMARY KEY AUTO_INCREMENT", sender="INT", recipient="INT", amount="INT")

    # setting up loop variables and user data
    running = True
    loggedIn = False
    username = ""
    balance = 0
    id = 0
    first = ""
    last = ""
    email = ""

    # main loop
    while running:
        # printing the menu
        printMenu(loggedIn, username=username, balance=balance)
        choice = input("Enter your choice: ")

        # Create account
        if choice == "1" and not loggedIn:
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            valid_email = False
            email = ""

            while not valid_email:
                email = input("Enter your email (Press 0 to quit): ")
                if email == "0":
                    break
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    valid_email = True
                else:
                    print("Invalid email format. Please try again.")
            if email == "0":
                continue

            username = input("Enter your desired username: ")
            password = input("Enter your desired password: ")
            create_account(first, last, email, username, password, newDB, "users")
            print("Account created successfully!")

        # Login
        elif choice == "2" and not loggedIn:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if login(username, password, newDB, "users"):
                loggedIn = True
                username = username
                data = newDB.fetchEntry("users", {"username": username}, "*").split(", ")
                id = int(data[0])
                first = data[1]
                last = data[2]
                email = data[3]
                balance = int(data[6]) if data[6] else 0

                
            else:
                print("Login failed. Please check your username and password.")

        # Deposit
        elif choice == "3" and loggedIn:
            if loggedIn:
                amount = 0
                try:
                    amount = int(input("Enter the amount to deposit: "))
                    if amount <= 0:
                        print("Please enter a positive amount to deposit.")
                        continue

                    if deposit(id, amount, balance, newDB, "users"):
                        print("Deposit successful!")
                        balance += amount
                    else:
                        print("Deposit failed. Please try again.")
                except ValueError:
                    print("Invalid input. Deposit unsuccessful.")
                    continue   
            else:
                print("Please log in to deposit funds.")

        # Withdraw
        elif choice == "4" and loggedIn:
            if loggedIn:
                amount = 0
                try:
                    amount = int(input("Enter the amount to withdraw: "))
                    if amount <= 0:
                        print("Please enter a positive amount to withdraw.")
                        continue

                    if withdraw(id, amount, balance, newDB, "users"):
                        print("Withdrawal successful!")
                        balance -= amount
                    else:
                        print("Withdrawal failed. Please check your balance and try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
            else:
                print("Please log in to withdraw funds.")

        # Transfer
        elif choice == "5" and loggedIn:
            target_username = input("Enter the recipient's username: ")
            amount = 0
            try:
                amount = int(input("Enter the amount to transfer: "))
                if amount <= 0:
                        print("Please enter a positive amount to transfer.")
                        continue

                recipient_id = newDB.fetchEntry("users", {"username": target_username}, "id")

                if id and recipient_id:
                    if transfer(id, recipient_id, amount, balance, newDB, "users"):
                        print("Transfer successful!")
                        balance -= amount
                        newDB.insertData("transactions", sender=id, recipient=recipient_id, amount=amount)
                    else:
                        print("Transfer failed. Please check your balance and try again.")
            except ValueError:
                print("Transfer failed. Please enter a valid number.")
                continue
        
        # Logout
        elif choice == "6" and loggedIn:
            print("Logging out...")
            loggedIn = False
            username = ""
            balance = 0
            id = 0
            first = ""
            last = ""
            email = ""

        elif choice == "7" and loggedIn:
            newDB.deleteData("users", {"id": id})
            print(f"Account {username} with id {id} deleted successfully")
            newDB.modifyData("transactions", {"sender": id}, {"sender": 0}) # Set sender to 0 for transactions where the deleted user was the sender
            newDB.modifyData("transactions", {"recipient": id}, {"recipient": 0}) # Set recipient to 0 for transactions where the deleted user was the recipient
            loggedIn = False
            username = ""
            balance = 0
            id = 0
            first = ""
            last = ""
            email = ""
        
        # Exit
        elif choice == "8":
            print("Thank you for using the Bank System. Goodbye!")
            running = False

        # Print tables for visualization
        elif choice == "9":
            newDB.printData("users")
            newDB.printData("transactions")


        else:
            print("Invalid choice. Please try again.")


    # Sample code to create accounts and perform transactions for testing purposes. This section can be uncommented to populate the database with sample data.
    """
    for user in users:
        try:
            create_account(user[0], user[1], user[2], user[3], user[4], newDB, "users")
            id = newDB.fetchEntry("users", {"username": user[3]}, "id")
            deposit(id, user[5], 0, newDB, "users")
            print("Account created for {} {} with username '{}' and balance ${}".format(user[0], user[1], user[3], user[5]))

        except Exception as e:
            print("Error creating account for {} {}: {}".format(user[0], user[1], e))
    """

    newDB.closeConnection()
    #newDB.deleteDB()
    #print(f"Database {newDB.dbName} deleted successfully")
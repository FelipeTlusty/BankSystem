# BankSystem
This is a command-line application that simulates a bank system written in Python and using mySQL to store and manage user information. The application includes operations such as creating a new account, log in, deposit, withdraw, and transfer of currencies, logout and closing of the account. The application also includes a print option for visualization of the database during operations.

# Requirements
1. Python 3.
2. pymysql for creating and connecting to the Database (pip install pymysql).
3. mySQL installed and an username and password created for mySQL.

# Installation
1. Install Python and pymysql.
2. Install mySQL and create a username and password.
3. Open main.py in a text editor and configure the Database variables to be able to connect to the Database.
4. Save the file.

# Usage
1. Open command prompt and navigate to the directory where you saved the files.
2. Run the command >py main.py.
3. Follow the instruction on-screen to use the app.

# Demo
Here's an example of how the code works:

'''
#===========================================#
#                                           #
#           Choose Your Action:             #
#           1. Create Account               #
#           2. Login                        #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 1
Enter your first name: demo
Enter your last name: example
Enter your email (Press 0 to quit): demo@email.com
Enter your desired username: demo
Enter your desired password: 123456
Account created successfully!
#===========================================#
#                                           #
#           Choose Your Action:             #
#           1. Create Account               #
#           2. Login                        #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 2
Enter your username: demo
Enter your password: 123456
#===========================================#
#           Welcome to the Bank!            #
#                                           #
#           Logged in as: demo              #
#           Current Balance: $0             #
#                                           #
#           Choose Your Action:             #
#           3. Deposit                      #
#           4. Withdraw                     #
#           5. Transfer                     #
#           6. Logout                       #
#           7. Close Account                #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 3
Enter the amount to deposit: 35475
Deposit successful!
#===========================================#
#           Welcome to the Bank!            #
#                                           #
#           Logged in as: demo              #
#           Current Balance: $35475         #
#                                           #
#           Choose Your Action:             #
#           3. Deposit                      #
#           4. Withdraw                     #
#           5. Transfer                     #
#           6. Logout                       #
#           7. Close Account                #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 4
Enter the amount to withdraw: 1495
Withdrawal successful!
#===========================================#
#           Welcome to the Bank!            #
#                                           #
#           Logged in as: demo              #
#           Current Balance: $33980         #
#                                           #
#           Choose Your Action:             #
#           3. Deposit                      #
#           4. Withdraw                     #
#           5. Transfer                     #
#           6. Logout                       #
#           7. Close Account                #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 5
Enter the recipient's username: felipe
Enter the amount to transfer: 4738
Transfer successful!
#===========================================#
#           Welcome to the Bank!            #
#                                           #
#           Logged in as: demo              #
#           Current Balance: $29242         #
#                                           #
#           Choose Your Action:             #
#           3. Deposit                      #
#           4. Withdraw                     #
#           5. Transfer                     #
#           6. Logout                       #
#           7. Close Account                #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 9
+----+------------+---------+--------------------------+----------+-------------+---------+
| id | first      | last    | email                    | username | password    | balance |
+----+------------+---------+--------------------------+----------+-------------+---------+
| 1  | felipe     | tlusty  | felipe@email.com         | felipe   | 123         | 13238   |
| 2  | diego      | costa   | diego@email.com          | diego    | 234         | 20000   |
| 3  | john       | doe     | jdoe@gmail.com           | jdoe     | password123 | 1000    |
| 4  | jane       | doe     | janedoe@gmail.com        | janedoe  | password321 | 2000    |
| 5  | bob        | smith   | bsmith@gmail.com         | bsmith   | password213 | 100     |
| 6  | alice      | smith   | asmith@gmail.com         | asmith   | password312 | 18500   |
| 7  | charlie    | brown   | charliebrownjr@gmail.com | cbrown   | password231 | 3726    |
| 8  | lucy       | brown   | lbrown@gmail.com         | lbrown   | password132 | 4828    |
| 9  | snoopy     | brown   | snoopdawg@gmail.com      | snoopy   | password321 | 1928    |
| 10 | linus      | brown   | linustechtips@gmail.com  | linus    | password213 | 377984  |
| 11 | sally      | brown   | sally@gmail.com          | sally    | password123 | 28882   |
| 12 | peppermint | patty   | pp@gmail.com             | ppatty   | password321 | 102938  |
| 15 | demo       | example | demo@email.com           | demo     | 123456      | 29242   |
+----+------------+---------+--------------------------+----------+-------------+---------+
+----+--------+-----------+--------+
| id | sender | recipient | amount |
+----+--------+-----------+--------+
| 1  | 2      | 1         | 3500   |
| 2  | 10     | 11        | 25000  |
| 3  | 0      | 1         | 5000   |
| 4  | 0      | 2         | 10000  |
| 5  | 1      | 0         | 1500   |
| 6  | 0      | 6         | 8500   |
| 7  | 15     | 1         | 4738   |
+----+--------+-----------+--------+
#===========================================#
#           Welcome to the Bank!            #
#                                           #
#           Logged in as: demo              #
#           Current Balance: $29242         #
#                                           #
#           Choose Your Action:             #
#           3. Deposit                      #
#           4. Withdraw                     #
#           5. Transfer                     #
#           6. Logout                       #
#           7. Close Account                #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 6
Logging out...
#===========================================#
#                                           #
#           Choose Your Action:             #
#           1. Create Account               #
#           2. Login                        #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 2
Enter your username: demo
Enter your password: 123456
#===========================================#
#           Welcome to the Bank!            #
#                                           #
#           Logged in as: demo              #
#           Current Balance: $29242         #
#                                           #
#           Choose Your Action:             #
#           3. Deposit                      #
#           4. Withdraw                     #
#           5. Transfer                     #
#           6. Logout                       #
#           7. Close Account                #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 7
Account demo with id 15 deleted successfully
#===========================================#
#                                           #
#           Choose Your Action:             #
#           1. Create Account               #
#           2. Login                        #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 9
+----+------------+--------+--------------------------+----------+-------------+---------+
| id | first      | last   | email                    | username | password    | balance |
+----+------------+--------+--------------------------+----------+-------------+---------+
| 1  | felipe     | tlusty | felipe@email.com         | felipe   | 123         | 13238   |
| 2  | diego      | costa  | diego@email.com          | diego    | 234         | 20000   |
| 3  | john       | doe    | jdoe@gmail.com           | jdoe     | password123 | 1000    |
| 4  | jane       | doe    | janedoe@gmail.com        | janedoe  | password321 | 2000    |
| 5  | bob        | smith  | bsmith@gmail.com         | bsmith   | password213 | 100     |
| 6  | alice      | smith  | asmith@gmail.com         | asmith   | password312 | 18500   |
| 7  | charlie    | brown  | charliebrownjr@gmail.com | cbrown   | password231 | 3726    |
| 8  | lucy       | brown  | lbrown@gmail.com         | lbrown   | password132 | 4828    |
| 9  | snoopy     | brown  | snoopdawg@gmail.com      | snoopy   | password321 | 1928    |
| 10 | linus      | brown  | linustechtips@gmail.com  | linus    | password213 | 377984  |
| 11 | sally      | brown  | sally@gmail.com          | sally    | password123 | 28882   |
| 12 | peppermint | patty  | pp@gmail.com             | ppatty   | password321 | 102938  |
+----+------------+--------+--------------------------+----------+-------------+---------+
+----+--------+-----------+--------+
| id | sender | recipient | amount |
+----+--------+-----------+--------+
| 1  | 2      | 1         | 3500   |
| 2  | 10     | 11        | 25000  |
| 3  | 0      | 1         | 5000   |
| 4  | 0      | 2         | 10000  |
| 5  | 1      | 0         | 1500   |
| 6  | 0      | 6         | 8500   |
| 7  | 0      | 1         | 4738   |
+----+--------+-----------+--------+
#===========================================#
#                                           #
#           Choose Your Action:             #
#           1. Create Account               #
#           2. Login                        #
#           8. Exit                         #
#           9. Print                        #
#                                           #
#===========================================#
Enter your choice: 8
Thank you for using the Bank System. Goodbye!
'''

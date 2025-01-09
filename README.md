#Banking System Project
This project is a simple Banking System implemented in Python using Object-Oriented Programming (OOP) principles. It provides functionalities for users to manage their accounts and for the bank admin to monitor overall account statistics.

#Features
#User Operations
#Open a New Account
Users can create a new bank account with a unique 3-digit account number.
#Login
Users can log in using their account holder name and account number.
#Deposit Money
Users can add money to their account balance.
#Withdraw Money
Users can withdraw money from their account, provided they have sufficient balance.
#Check Balance
Users can view their current account balance.
#Transfer Money
Users can transfer funds to another account by providing the recipient's account number.
#View Transaction History
Users can see their detailed transaction history, including timestamps.
#Admin Operations
#View Total Deposits
Admins can check the total money deposited in the bank across all accounts.
#View Total Number of Accounts
Admins can see the total number of accounts in the bank.
#How It Works
Each account is assigned a unique 3-digit account number during account creation.
Users can log in using their account holder name and account number for enhanced security.
Transactions (deposits, withdrawals, transfers) are recorded with timestamps, providing a detailed history for every account.
#Limitations
#Data Persistence
Currently, the project does not include file-based storage or a database to save account and transaction data. All data is stored in memory during program execution and is lost once the program ends.

Reason: Filing was not mentioned as a requirement in the original project scope.

#Future Enhancements
#Add File-Based Storage
Save account and transaction data to a file (e.g., JSON, CSV, or database) to ensure data persistence.
#User Authentication
Implement secure login with passwords for better security.
#Account Types
Support for account types like savings and current, with different features.
#Interest Calculation
Add periodic interest for savings accounts.
#GUI Integration
Develop a graphical user interface for ease of use.

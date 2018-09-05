# wallet
Mpaani Wallet Assignment (Rest APIs , using Django)

Install Python

# Gather Dependencies
pip install -r pipfile.txt

# Create Database
python manage.py migrate

# Start Server
python manage.py runserver

To create new User, POST
http://localhost:8000/api/v1/user/create/

To login as a user and retreive token, POST
http://localhost:8000/api/v1/user/login/



TOKEN required

To logout as a user, POST
http://localhost:8000/api/v1/user/logout/

View User Profile,GET
http://localhost:8000/api/v1/user/

View User Wallets,GET
http://localhost:8000/api/v1/user/1/wallet/

Create new Wallet for logged in user, Post
http://localhost:8000/api/v1/user/1/wallet/create/

Create a new Transaction , Post
http://localhost:8000/api/v1/user/1/wallet/1/transaction  

Cancel a transaction, Delete
http://localhost:8000/api/v1/user/1/wallet/1/transaction/MPAANI_1

View Passbook for your wallet, GET
http://localhost:8000/api/v1/user/1/wallet/1/
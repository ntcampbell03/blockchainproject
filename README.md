# blockchainproject

Cryptocurrency

Website

<<<<<<< HEAD
NEW WAY TO RESET DB
step 1: clear postgres db
step 2: set init blockchain object to false
step 3: run dbinit.py
step 4: set init blockchain object to true
=======
Creating db:

python3
> from coin import db
> db.create_all()
> exit()

To check if its workings right
cd coin
sqlite3 db.sqlite3
.tables

if it works it will list the tables

<small>Trans: {{ trans.amount }}</small> <br>
<small>Sender: {{ trans.sender.name }}</small> <br>
<small>Reciever: {{ trans.reciever.name }}</small> 
>>>>>>> 63d400a1d17fce207c98fb3e61fbf443358310d4

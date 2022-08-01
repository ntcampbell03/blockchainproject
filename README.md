# blockchainproject

Cryptocurrency



Website

Creating db:

python3
> from coin import db
> db.create_all()
> exit()

To check if its workings right
cd coin
sqlite3 db.sqlite3
.tables

NEW WAY TO RESET DB
step 1: clear postgres db
step 2: set init blockchain object to false
step 3: run dbinit.py
step 4: set init blockchain object to true

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

if it works it will list the tables

<small>Trans: {{ trans.amount }}</small> <br>
<small>Sender: {{ trans.sender.name }}</small> <br>
<small>Reciever: {{ trans.reciever.name }}</small> 

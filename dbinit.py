from blockchainJson import *

# ======CLEAR TABLE======

# conn = get_db_connection()
# cur = conn.cursor()
# cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public'")
# tables = cur.fetchall()
# print(tables)
# for table in tables:
#     cur.execute(f"DELETE FROM {table[0]}")
# for table in tables:
#     cur.execute(f"DROP TABLE {table[0]}")
# conn.commit()

# ======INIT  TABLE======

from coin import db
from coin import app

with app.app_context():
    db.create_all()
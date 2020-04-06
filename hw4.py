import sqlite3 as sql
from pymemcache.client import base

Name = 'Apple'

client = base.Client(('localhost', 11211))
result = client.get(Name)

def query_db(Name):
    db_connection = sql.connect('db.sql')
    c = db_connection.cursor()
    try:
        c.execute('select Description from my_table1 where Name = "{k}"'.format(k=Name))
        data = c.fetchone()[0]
        db_connection.close()
    except:
        data = 'invalid'
    return data

if result is None:
    print("It’s a MISS, getting it from database")
    result = query_db(Name)
    if result == 'invalid':
        print("Requested data is not in db")
    else:
        print("Displaying data to client from db")
        print("=> Product: {p}, Description: {d}".format(p=Name, d=result))
        print("Adding the data to memcache")
        client.set(Name, result)

else:
    print("Displaying data directly from memcache")
    print("=> Product: {p}, Description: {d}".format(p=Name, d=result))

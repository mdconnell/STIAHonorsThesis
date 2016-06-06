from tinydb import TinyDB, Query
import sqlite3

db = TinyDB('db1.json')


def get_users_in_database():
    counter = 1
    conn = sqlite3.connect('twitter_project.db')
    c = conn.cursor()
    query = "",
    c.execute("select * from tweets")
    for id, user, text, location, timestamp, json in c.fetchall():
        print counter
        counter +=1
        db.insert({'id': id, 'user': user, 'location': location, 'timestamp': timestamp, 'json': json})
    print db.all
print len(db.search(Query()['json']['user'] != None))
#get_users_in_database()
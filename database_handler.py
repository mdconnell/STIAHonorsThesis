__author__ = 'marcconnell95'
import sqlite3
import operator
import unidecode
#does not cover database generation
def create_database():
    conn = sqlite3.connect('twitter_project.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users
             (user, tweetIDs)''')

#create_database()

def open_database():
    conn = sqlite3.connect('twitter_project.db')
    c = conn.cursor()
"""
def add_user(tweet, cursor, conn):
    print "add_user"
    fields = tweet['user']['screen_name'], tweet['id']
    cursor.execute("INSERT INTO users VALUES (?,?)", fields)
    conn.commit()

def add_tweet_to_tweetIDs(tweet, cursor, conn):
    #user = tweet['user']['screen_name'],
    user = "SandrineMeraud",
    cursor.execute("select tweetIDs from users where user=?", user)[0]
    tweetIDs = cursor.fetchall()
    #new_tweet = tweet['id']+","
    new_tweet = "new_tweet"+","
    tweetIDs = tweetIDs+new_tweet
    cursor.execute("UPDATE users SET tweetIDs=? WHERE user=?", (tweetIDs,user))
    print cursor.fetchall()
    print "add_tweet_to_tweetIDs"
add_tweet_to_tweetIDs("foo", sqlite3.connect('twitter_project.db').cursor() ,sqlite3.connect('twitter_project.db'))

def check_if_user_in_db(tweet, cursor, conn):
    print "check_if_user_in_db"
    screen_name = tweet['user']['screen_name'],
    print screen_name
    cursor.execute("select user from users where user=?", screen_name)
    data = cursor.fetchall()
    if not data:
        add_user(tweet, cursor, conn)
    else:
        add_tweet_to_tweetIDs(tweet, cursor, conn)
"""
def add_tweet(tweet):
    #print str(tweet)
    conn = sqlite3.connect('twitter_project.db')
    cursor = conn.cursor()
    fields = tweet['id'], tweet['user']['screen_name'], tweet['text'], tweet['user']['location'], tweet['created_at'], str(tweet)
    cursor.execute("INSERT INTO tweets VALUES (?,?,?,?,?,?)", fields)
    #check_if_user_in_db(tweet, cursor, conn)
    conn.commit()

def get_users_in_database():
    conn = sqlite3.connect('twitter_project.db')
    c = conn.cursor()
    query = "",
    c.execute("select * from tweets")
    user_dict = {}
    for each in c.fetchall():
        user = each[1]
        if user in user_dict:
            user_dict[user] += 1
        else:
            user_dict[user] = 1
    for each in user_dict.keys():
        print str(each)+": "+str(user_dict[each])

    print "total unique users: "+str(len(user_dict.keys()))

def get_unique_tweets():
    conn = sqlite3.connect('twitter_project.db')
    c = conn.cursor()
    c.execute("select * from tweets")
    tweet_dict = {}
    for each in c.fetchall():
        user = unidecode.unidecode_expect_nonascii(each[2][0:15])

        if user[0:4] == "RT @":
            user = user[4:]
        if user in tweet_dict:
            tweet_dict[user] +=1
        else:
            tweet_dict[user] = 1
    for each in tweet_dict.keys():
        print str(each)+": "+str(tweet_dict[each])

    print "total unique tweets: "+str(len(tweet_dict.keys()))
#get_unique_tweets()
#get_users_in_database()
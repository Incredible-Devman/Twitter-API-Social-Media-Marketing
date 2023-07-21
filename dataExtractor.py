import sqlite3
import tweepy
import time


con=sqlite3.connect("example1.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS twitter_data(id, tweet, date, retweet, favorite, reply, brand, hashtags, links, media)")
con.commit()
handles = ["Unilever", "Lu"]
for hndl in handles:
    for status in tweepy.Cursor(api.user_timeline, id=hndl).items(50):
        tw_id=status.id
        tweet=status.text.replace("\n", "").replace("\r","").replace("\r\n","")
        date=status.created_at
        retweet=status.retweet_count
        favorite=status.favorite_count
        reply=status.in_reply_to_screen_name
        brand=status.user.screen_name

        hashtaglist=[]
        try:
            for hashtag in status.entities["hashtags"]:
                hahstaglist.append(hashtag["text"])

        except:
            pass
        hashtags=", ".join(hashtaglist)

        linklist=[]
        try:
            for link in status.entities["url"]:
                linklist.append(link["expanded_url"])

        except:
            pass
        links=", ".join(linklist)

        medialist=[]
        try:
            for media in status.entities["media"]:
                medialist.append(media["expanded_url"])

        except:
            pass
        medias=", ".join(medialist)

    cur.execute("INSERT INTO twitter_data VALUES(?,?,?,?,?,?,?,?,?,?)",(tw_id, tweet, date, retweet, favorite, reply, brand, hashtags,links, medias))
    con.commit()
    time.sleep(1)

user_h = api.get_user("Unilever")
print(user_h.statuses_count)
print(user_h.followers_count)
print(user_h.friends_count)

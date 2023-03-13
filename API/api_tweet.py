from bottle import post, request, response
import uuid
import time
import x

@post("/")
def _():
    try:
        x.validate_tweet()
        db = x.db()
        tweet_id = str(uuid.uuid4().hex)
        tweet_user_fk = "cdd0a0a3be06427f84111a767e9729f9"
        tweet_created_at = int(time.time())
        tweet_message = request.forms.get("message")
        tweet_image = ""
        tweet_updated_at = int(time.time())
        tweet_total_retweets = "0"
        tweet_total_likes = "0"
        tweet_total_views = "0"
        tweet_total_replies = "0"

        db.execute("INSERT INTO tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (tweet_id,tweet_user_fk,tweet_created_at, tweet_message, tweet_image,tweet_updated_at, tweet_total_retweets,tweet_total_likes,tweet_total_views,tweet_total_replies))
        db.commit()

        return {"info":"ok", "tweet_id":tweet_id,
                "tweet_created_at":tweet_created_at,
                "tweet_total_replies":tweet_total_replies,
                "tweet_total_likes":tweet_total_likes,
                "tweet_total_views":tweet_total_views,
                "tweet_total_retweets":tweet_total_retweets}
    except Exception as ex:
        response.status = 400
        return {"info":str(ex)}
    finally:
        if "db" in locals(): db.close()
from bottle import get, template
import x

tweets = []

@get("/new_tweets")
def _():
    return template("new_tweets", tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN, tweets=tweets)
# https://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@github.com/emil7809/twitter.git
#lålå

from bottle import default_app, get, run, template, static_file, post, response, request
import x
import sqlite3
import pathlib
import git
import bridge_login
import api.api_tweet



trends = [
    {"title": "Norge", "total_tweets": "1,693"},
    {"title": "Otto", "total_tweets": "20K"}
]

@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./twitter')
  origin = repo.remotes.origin
  repo.create_head('Master', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""



@get("/")
def _():
    try:
        response.add_header("Cache-Control", "no-cashe, no-store, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cashe")
        response.add_header("Expires", 0)
        me = request.get_cookie("user", secret="my-secret")
        #db = sqlite3.connect(
        #    str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        #db.row_factory = dict_factory
        db = x.db()
        #tweets = db.execute("SELECT * FROM tweets").fetchall()
        users = db.execute("SELECT * FROM users").fetchall()
        # print(tweets)
        #print(users)
        users_and_tweets = db.execute(
            'SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk ORDER BY tweet_created_at DESC LIMIT 0, 10').fetchall()
        #print("#"*30)
        #print(users_and_tweets)

        return template("index", me=me, trends=trends, users_and_tweets=users_and_tweets, users=users, tweet_min_len=x.TWEET_MIN_LEN, tweet_max_len=x.TWEET_MAX_LEN)

    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals():
            db.close()


@get("/login")
def _():
    return template("login")


@get("/logout")
def _():
    response.set_cookie("user", "", expires=0)
    response.status=303
    response.set_header("Location", "/")
    return 

@get("/<username>")
def _(username):
    try:
        response.add_header("Cache-Control", "no-cashe, no-store, must-revalidate, max-age=0")
        response.add_header("Pragma", "no-cashe")
        response.add_header("Expires", 0)
        me = request.get_cookie("user", secret="my-secret")
        db = x.db()
        users = db.execute("SELECT * FROM users").fetchall()
        user = db.execute(
            "SELECT * FROM users WHERE user_username=? COLLATE NOCASE", (username,)).fetchall()[0]

        user_id = user["user_id"]
        user_name = user["user_username"]
       
        
        users_and_tweets = db.execute(
            'SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk WHERE tweet_user_fk=? ORDER BY tweet_created_at DESC LIMIT 0, 10', (user_id,)).fetchall()

        return template("profile", me=me, user=user, users=users, trends=trends, title=user_name, users_and_tweets=users_and_tweets)
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals():
            db.close()


@get("/style.css")
def _():
    return static_file("style.css", root=".")

@get("/js/validate.js")
def _():
    return static_file("validate.js", root="./js")

@get("/js/app.js")
def _():
    return static_file("app.js", root="./js")

@get("/avatars/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./avatars")

@get("/tweet_images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./tweet_images")

@get("/user_cover/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./user_cover")

try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=80, debug=True, reloader=True)

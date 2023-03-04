# https://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@github.com/emil7809/twitter.git

from bottle import default_app, get, run, template, static_file, post
import sqlite3
import pathlib
import git

##############################


def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

##############################


trends = [
    {"title": "Norge", "total_tweets": "1,693"},
    {"title": "Otto", "total_tweets": "20K"}
]

@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./twitter')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""



@get("/")
def _():
    try:
        db = sqlite3.connect(
            str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory

        #tweets = db.execute("SELECT * FROM tweets").fetchall()
        #users = db.execute("SELECT * FROM users").fetchall()
        # print(tweets)
        #print(users)
        users_and_tweets = db.execute(
            'SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk').fetchall()
        print("#"*30)
        print(users_and_tweets)

        return template("index", trends=trends, users_and_tweets=users_and_tweets)

    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals():
            db.close()


@get("/<username>")
def _(username):
    try:
        db = sqlite3.connect(
            str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
        db.row_factory = dict_factory
        users = db.execute("SELECT * FROM users").fetchall()
        user = db.execute(
            "SELECT * FROM users WHERE user_username=? COLLATE NOCASE", (username,)).fetchall()[0]

        user_id = user["user_id"]
        user_name = user["user_username"]
        tweets = db.execute(
            "SELECT * FROM tweets WHERE tweet_user_fk=?", (user_id,)).fetchall()

        return template("profile", user=user, users=users, trends=trends, tweets=tweets, title=user_name)
    except Exception as ex:
        print(ex)
        return "error"
    finally:
        if "db" in locals():
            db.close()


@get("/style.css")
def _():
    return static_file("style.css", root=".")


@get("/avatars/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./avatars")

try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=80, debug=True, reloader=True)

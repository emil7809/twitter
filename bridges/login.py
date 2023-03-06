from bottle import default_app, get, run, request, response, template, static_file, post
import sqlite3
import pathlib

##############################


def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}

##############################


@post("/login_page")
def _():
    # Redirection
    # response.set_header("Location", "/login")
    user_x = {
        "user_name":"emilyhoolahan",
        "user_first_name":"Emily",
        "user_last_name":"Hoolahan"
    }

    db = sqlite3.connect(
            str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory

        #tweets = db.execute("SELECT * FROM tweets").fetchall()
    user = db.execute("SELECT * FROM users").fetchall()[0]
    print("#"*30)
    print(user)
    print("#"*30)
    # cookie_experation_date = int(time.time())+ 7200
    response.set_cookie("user", user, secret="my-secret", httponly=True)
    response.status = 303
    response.set_header("Location", "/")
    return "This is the bridge"

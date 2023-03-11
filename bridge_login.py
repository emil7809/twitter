from bottle import post, response

@post("/login")
def _():
    user_x = {
        "user_name":"emilyhoolahanxxx",
        "user_first_name":"EmilyXXX",
        "user_last_name":"HoolahanXXX"
    }

    # cookie_experation_date = int(time.time())+ 7200
    response.set_cookie("user", user_x, secret="my-secret", httponly=True)
    response.status = 303
    #response.set_header("Location", "/bridge_login")
    response.set_header("Location", "/")
    return "This is the bridge"
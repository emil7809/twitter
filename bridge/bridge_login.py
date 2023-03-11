from bottle import post, response

@post("/login")
def _():
    return "This is the bridge"
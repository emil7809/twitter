from bottle import post, request, response
import x

@post("/api-login")
def _():
    try:
        user = request.get_cookie("user", secret=x.MY_COOKIE_SECRET)
        if user: return {"info":"Success login", "user_name":user["user_name"]}
        user_email = x.validate_email()
        db = x.db()
        user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()
        if not user: raise Exception(400, "Can't login")
        try:
            import production
            is_cookie_https = True
        except:
            is_cookie_https = False
        response.set_cookie("user", user, secret=x.MY_COOKIE_SECRET, httponly=True, secure=is_cookie_https)
        return {"info":"success login", "user_name":user["user_name"]}
    except Exception as ex:
        print(ex)
    finally:
        if "db" in locals(): db.close()
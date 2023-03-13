from bottle import post, request, response
import x

@post("/api-sign-up")
def _():
    try:
        user_username = x.validate_user_username()
        user_id = 1
        user = {
            "user_id":user_id,
            "user_username" : user_username
        }
        values = ""
        for key in user:
            values = values + f":{key},"
        values = values.rstrip(",")
        print(values)
        
        #db = x.db
        #db.execute(f"INSERT INTO users VALUES({values})", user )
        return "try ok"
    except Exception as ex:
        print(ex)
        response.status = 400
        return {"info":str(ex)}
    finally:
        pass
    
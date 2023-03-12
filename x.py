from bottle import request, response
import sqlite3
import pathlib
import re

##############################

def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db")
    db.row_factory = dict_factory
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass


##############################

TWEET_MIN_LEN = 1
TWEET_MAX_LEN = 280

def validate_tweet():
  error = f"Meassage must be between {TWEET_MIN_LEN} and {TWEET_MAX_LEN} characters"
  if len(request.forms.message) < TWEET_MIN_LEN: raise Exception(error)
  if len(request.forms.message) > TWEET_MAX_LEN: raise Exception(error)
  return request.forms.message

##############################

##############################

EMAIL_MIN = 6
EMAIL_MAX = 150
EMAIL_REGEX = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"

def validate_email():
  error = f"email must be between {EMAIL_MIN} and {EMAIL_MAX} characters, and must include @"
  request.forms.user_email = request.forms.user_email.strip()
  if len(request.forms.user_email) < EMAIL_MIN: raise Exception(error)
  if len(request.forms.user_email) > EMAIL_MAX: raise Exception(error)
  if not re.match(EMAIL_REGEX, request.forms.user_email):raise Exception(error)
  return request.forms.user_email

##############################

##############################

PASSWORD_MIN_LEN = 5

def validate_password():
  error = f"You'r Password must be at least {PASSWORD_MIN_LEN} characters"
  if len(request.forms.user_password) < PASSWORD_MIN_LEN: raise Exception(error)
  return request.forms.get.user_password

##############################

##############################

MY_COOKIE_SECRET = "!L+h3XE2oXli7KC4eQM/pGg==?gAWVaQAAAAAAAACMBHVzZXKUfZQojAl1c2VyX25hbWWUjBBlbWlseWhvb2xhaGFueHh4lIwPdXNlcl9maXJzdF9uYW1llIwIRW1pbHlYWFiUjA51c2VyX2xhc3RfbmFtZZSMC0hvb2xhaGFuWFhYlHWGlC4="

def validate_user_logged():
  user = request.get_cookie("user", secret=MY_COOKIE_SECRET)
  if user is None: raise Exception(400, "user must be logged in")
  return user

##############################


 
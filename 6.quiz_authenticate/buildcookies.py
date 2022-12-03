#!/usr/bin/python3
from credentials import *
from host import *
import requests
import json


api = "api/account/login/"
url=host+api
s = "cookies = [\n"
while(len(USER_CREDENTIALS) != 0):
    email,password = USER_CREDENTIALS.pop()
    data={
        "email_id":email,"passcode":password
    }
    r=requests.post(url,data=data)
    cookiejar = r.cookies
    cookies = json.dumps(dict(cookiejar))
    auxcookies={}
    auxcookies[email]=cookies
    finalcookie = json.dumps(auxcookies)
    s = s + finalcookie +",\n"
    print(email)
s = s+"]"
f= open("cookies.py","w")
f.write(s)
f.close()
print("done")
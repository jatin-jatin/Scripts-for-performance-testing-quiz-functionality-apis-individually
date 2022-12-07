#!/usr/bin/python3
import json
from traceback import print_tb
import requests
import re
from cookies import cookies
from quizid import quizid
from host import host

s="keystate={\n"

api = "api/quiz/"+ quizid + "/info/"
url = host + api
while(len(cookies)!=0):
    usrcookie = cookies.pop()
    email=list(usrcookie)[0]
    cookiejar=usrcookie[email]
    cookiejar = json.loads(cookiejar)
    r = requests.get(url,cookies=cookiejar)
    print(r.content)
    quiz_keystate = re.search(r"\"keystate\":(.*?)(,|})",r.text)
    quiz_keystate=quiz_keystate.group(1)[1:-1]
    # key={}
    # key[email]=quiz_keystate
    keystring = '"'+email+'"' +':'+'"'+quiz_keystate+'"'
    s=s+keystring+",\n"
s=s+"}"
f=open("keystate.py","w")
f.write(s)
f.close()
print("done")
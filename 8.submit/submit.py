from keystate import keystate
from host import host
from cookies import cookies
from locust import HttpUser,SequentialTaskSet,task,constant,log
from Answers import answers
import json
import datetime

class SafeLogin(SequentialTaskSet):
    def __init__(self,parent):
        super().__init__(parent)
        cookiedict=cookies.pop()
        email = list(cookiedict)[0]
        cookiestring = cookiedict[list(cookiedict)[0]]
        self.cookiejar = json.loads(cookiestring)
        self.keystate = keystate[email]
        self.csrftoken = self.cookiejar["csrftoken"]

    @task
    def submit_quiz(self):
            url = "api/quiz/"+ self.keystate+ "/submit/"
            datetime_format = "%Y-%m-%dT%H:%M:%S"
            data ={
                "quizData":answers,"submissionTime":datetime.datetime.now().strftime(datetime_format),"seconds_since_mark":"0"
            }
            with self.client.post(url,name="submit_quiz",json=data,headers={"X-CSRFToken": self.csrftoken},cookies=self.cookiejar,catch_response=True) as response:
                print(url,response)

class MySeqTest(HttpUser):
    wait_time=constant(1)
    host=host
    tasks = [SafeLogin]
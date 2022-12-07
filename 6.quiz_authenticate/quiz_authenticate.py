from ..initial_configuration.quizid import quizid
from ..initial_configuration.host import host
from ..initial_configuration.cookies import cookies
import json
from locust import HttpUser,SequentialTaskSet,task,constant,log
class SafeLogin(SequentialTaskSet):
    def __init__(self,parent):
        super().__init__(parent)
        cookiedict=cookies.pop()
        cookiestring = cookiedict[list(cookiedict)[0]]
        self.cookiejar = json.loads(cookiestring)

    @task
    def authenticate_quiz(self):
            url = "api/quiz/"+ quizid + "/authenticate/"
            data=None
            with self.client.get(url,name="authenticate_quiz",cookies=self.cookiejar,catch_response=True) as response:
                print(url,response)
                print(response.content)

class MySeqTest(HttpUser):
    wait_time=constant(1)
    host=host
    tasks = [SafeLogin]
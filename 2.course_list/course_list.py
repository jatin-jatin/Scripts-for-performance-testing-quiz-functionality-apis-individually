import json
from ..initial_configuration.host import host
from ..initial_configuration.cookies import cookies 
from locust import HttpUser,SequentialTaskSet,task,constant,log
from locust.exception import StopUser
class SafeLogin(SequentialTaskSet):
    def __init__(self,parent):
        super().__init__(parent)
        cookiedict=cookies.pop()
        cookiestring = cookiedict[list(cookiedict)[0]]
        self.cookiejar = json.loads(cookiestring)

    @task
    def course_list(self):
            url ="api/course/"
            data=None
            with self.client.get(url,name="course_list",cookies=self.cookiejar,catch_response=True) as response:
                print(url,response)

class MySeqTest(HttpUser):
    wait_time=constant(1)
    host=host
    tasks = [SafeLogin]
from ..initial_configuration.host import host
from ..initial_configuration.cookies import cookies
import json
from locust import HttpUser,SequentialTaskSet,task,constant,log
from locust.exception import StopUser
class SafeLogin(SequentialTaskSet):
    def __init__(self,parent):
        super().__init__(parent)
        cookiedict=cookies.pop()
        cookiestring = cookiedict[list(cookiedict)[0]]
        self.cookiejar = json.loads(cookiestring)

    @task
    def upload_image_(self):
        url = "api/quiz/uploadImage/"
        attach = open('mid.jpg', 'rb')
        with self.client.post(url, name="upload_image", files=dict(ansimage=attach), headers={"X-CSRFToken": self.csrftoken},cookies=self.cookiejar,catch_response=True) as response:
            print(url+"done")

class MySeqTest(HttpUser):
    wait_time=constant(1)
    host=host
    tasks = [SafeLogin]
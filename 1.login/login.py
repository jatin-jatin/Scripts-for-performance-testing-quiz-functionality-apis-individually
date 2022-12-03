from host import host
from credentials import USER_CREDENTIALS
from locust import HttpUser,SequentialTaskSet,task,constant,log
from locust.exception import StopUser

class SafeLogin(SequentialTaskSet):
    def __init__(self,parent):
        super().__init__(parent)
        self.email,self.password=USER_CREDENTIALS.pop()

    @task
    def login(self):
            self.client.cookies.clear()
            url="api/account/login/"
            data={
                "email_id":self.email,"passcode":self.password
            }
            with self.client.post(url,name="login",data=data,catch_response=True) as response:
                print(url,response)
    @task
    def on_stop(self):
        raise StopUser()

class MySeqTest(HttpUser):
    wait_time=constant(1)
    host=host
    tasks = [SafeLogin]


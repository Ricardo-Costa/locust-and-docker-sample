from locust import HttpUser, TaskSet, task, between
 
class UserTasks(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/hello-world") # your target route

class WebsiteUser(HttpUser):
    stop_timeout = 30 # 30s limit timeout
    host = "http://localhost:3000/" # target host
    tasks = [UserTasks]

    def on_start(self):
        self.client.headers = {'X-Token': '123'}

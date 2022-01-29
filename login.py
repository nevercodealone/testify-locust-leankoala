import string
from locust import HttpUser, task, between

class Login(HttpUser):
    wait_time = between(1, 2)

    @task
    def wrongCredentials(self):
        with self.client.get("/secure_area/login_check", json={"_username": "notextist", "_password": "thisisnotworking", "_submit":"Log in"}, catch_response=True) as response:
            if response.status_code != 302:
                response.failure("Wrong resonse code: " + str(response.status_code))

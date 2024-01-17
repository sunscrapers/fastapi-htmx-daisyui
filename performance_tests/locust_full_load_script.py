from locust import HttpUser
from locust import between
from locust import task


class MyUser(HttpUser):
    wait_time = between(0.8, 1.2)  # Time between requests in seconds

    @task
    def fun_fact_full_load(self):
        self.client.get("/fun-fact-full-load")

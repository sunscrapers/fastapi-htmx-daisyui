from locust import HttpUser
from locust import between
from locust import task


class MyUser(HttpUser):
    wait_time = between(0.8, 1.2)  # Time between requests in seconds

    @task(1)
    def fun_fact_partial_load(self):
        self.client.get("/fun-fact-partial-load")

    @task(1)
    def fun_fact_partial_load_count(self):
        self.client.get("/fun-fact-partial-load-count")

    @task(1)
    def fun_fact_partial_load_footer(self):
        self.client.get("/fun-fact-partial-load-footer")

    @task(100)
    def fun_fact_partial_load_data(self):
        self.client.get("/fun-fact-partial-load-data")

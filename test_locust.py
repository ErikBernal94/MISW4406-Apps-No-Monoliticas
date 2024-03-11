from locust import HttpUser, task, between
import requests
import random


class Test(HttpUser):
    @task
    def submit(self):
        headers = {"Content-Type": "application/json "}

        print('Iniciando test')
        payload={
            "correo_electronico": "email@test.com",
            "direccion": "calle test",
            "id": random.randint(1,9999)
        }
        print(payload)
        r = self.client.post("http://34.102.177.23/bff/companias/registrar",headers=headers,json=payload)
        print(r)
        print('termino test')
import requests
from datetime import *
from requests.auth import HTTPBasicAuth
import os

WEIGHT = 45
HEIGHT = 155
AGE = 18

basic = HTTPBasicAuth('aslesham.social@gmail.com', 'ekta@123456')

os.environ["APP_ID"] = "ce13979c"
os.environ["APP_KEY"] = "8583427ed0b5bc05a320d6f86dcbd54a"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/55f9227d8d1fb79ef9a5ce1e93510660/myWorkoutTracker/sheet1"


headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["APP_KEY"]
}

exercise_done = input("Tell me the exercises you did today: ")

exercise_parameters = {
    "query": exercise_done,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

input_response = requests.post(url = exercise_endpoint, json = exercise_parameters, headers = headers)
data = input_response.json()
print(data)

now = datetime.now()
date = now.strftime("%d/%M/%Y")
time = now.strftime("%X")
print(time)

for exercise in data["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

post_response = requests.post(url = sheety_endpoint, json = sheet_inputs, auth=basic )
print(post_response.json())
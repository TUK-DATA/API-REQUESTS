import requests as request
import random
from time import sleep


post_url = "https://tukdata.herokuapp.com/data"

def generate_temperature():
    temperature = random.randrange(21,30,1)
    return temperature

def generate_humidity():
    humidity = random.randrange(20,100,3)
    return humidity

def estimate_airQuality():
    temp = generate_temperature()
    humidity = generate_humidity()
    if(humidity < 40):
        airQuality = "Harsh"
    else:
        airQuality = "Fair"

    return airQuality


def post(url,json_data):
    real_time_endpoint = "/real-time"
    real_time_url = url+real_time_endpoint
    response = request.post(url,json = json_data)
    real_time_response = request.post(real_time_url,json = json_data)
    return response,json_data






while(True):
    post_data = {
    "temperature":generate_temperature(),
    "humidity":generate_humidity(),
    "airQuality":estimate_airQuality()
}
    response,data = post(post_url,post_data)
    print(response)
    print(data)
    print("------------------------")
    
    sleep(2)
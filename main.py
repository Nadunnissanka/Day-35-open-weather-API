import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "58221932fa391385b252976ecdddf81f"
account_sid = "AC1769847cda015262b401e487fe9a8bf2"
auth_token = "161a43cf3a5fec3255aa69b7bff8b721"

parameters = {
    "lat": 6.847278,
    "lon": 79.926605,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"]
twelve_hr_weather_list = weather_data[0:12]

rain_is_coming = False

for weather in twelve_hr_weather_list:
    condition = weather["weather"][0]["id"]
    if condition < 700:
        rain_is_coming = True

if rain_is_coming:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="☂️ It's Going to Rain today! Remember to bring an Umbrella ☂️", from_='+14159937741',
                to='+94718136360')
    print(message.status)

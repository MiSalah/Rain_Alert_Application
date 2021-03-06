import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "AC18b9c98cc4ff5a660199d02bf4683e4f"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "33.270981", #Latitude & longtitude of your location
    "lon": "-7.584740",
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="Number phone from twilio", #purchase it from twilio, you can opt for a free number
        to="Your number phone"
    )
    print(message.sid)

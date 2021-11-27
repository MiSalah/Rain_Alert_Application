
# The Program Description. 

It's the winter. And when the snow falls the nature listens. Last days, did you ever feel upset cuz you didn't check the weather ? 

In fact, that happens to me betweenwhiles as well. However, with python everything can be automated. So, rather than checking the weather app every morning, This bunch of code will make it especially for you ! It's a python code program that checks the weather status instead of doing it manually ( i know how much lazy we're  ) and if it will rain in the next x hours, an SMS will be rendered to your phone to alert you that you need to be prepared for a running day. So, all you have to do is wait until the morning, and where there is a raining day there is a an Alert SMS.

# I used twilio as a SMS API and openweather for getting the weather conditions. 
## here are the two websites :

- #### Twilio : https://www.twilio.com/
- #### Openweather : https://openweathermap.org/

## To run the application : 

> * export OWM_API_KEY=YOUR OPENWHEATHER KEY HERE
> * export AUTH_TOKEN=YOUR AUTH TOKEN FROM TWILIO HERE
> * python3 app.py

## The SMS message : 

This is sms you'll get if it will rain in the next 8 hours of the current day!

![sms_rain](https://user-images.githubusercontent.com/74468388/143675389-562e0c0f-a4e2-44d2-a910-02092e2577e7.png)


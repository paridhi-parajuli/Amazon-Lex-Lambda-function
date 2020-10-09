
from urllib.request import Request, urlopen
import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get_weather_update(city):
  
    
    api_id = 'api_key'
    request = Request("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city,api_id))
    response = json.loads(urlopen(request).read())
    print(response)
    return response
  
  
def lambda_handler(event, context):
    
    logger.debug(event)
    city = event["currentIntent"]["slots"]["City"]
    
    weather = get_weather_update(city)
    weather_description = weather['weather'][0]['description']
    temp_current = weather['main']['feels_like'] 
    temp_high = weather['main']['temp_max'] 
    temp_low = weather['main']['temp_min']  
    
    return {
      "sessionAttributes": event["sessionAttributes"],
      "dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
          "contentType": "PlainText",
          "content":"Right now  in {} it is {} degree celcius and mostly {} with a forecasted high  and low of {} & {} degrees respectively.".format(city,temp_current,weather_description,temp_high,temp_low)
          },
        }
        }
            
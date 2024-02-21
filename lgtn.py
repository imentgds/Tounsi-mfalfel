import python_weather

import asyncio
import os
import random
R_EATING = "maneklchyy bot ranii chbiik sahbii !!\n wnty sadi9i chtekl"
def unknown():
    response = ['Wchyy',"chtahki ya maalem ??","Chto9seed ya shaybii ?","Chm3neha ya bro "] [random.randrange (4)]
    return response
def dbara():
    response = ["Tajine ","Coussksy","Ma9arunaa","Brickaa","Ojja tunisienne","Slata meshwiya"] [random.randrange (6)]
    return response

async def weather():

    async def getweather():
      # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
      async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a city
        weather = await client.get('Tunisia')
        
        # returns the current day's forecast temperature (int)
        return((weather.current.temperature - 32) * 5/9)
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    await asyncio.run(getweather())
def wzyr():
    return"Nizar Ben Néji (arabe : نزار بن ناجي), né le 27 juin 1981 à La Manouba1, est un homme politique et ingénieur tunisien, docteur en technologie de l'information et de la communication. Il est chargé du ministère des Technologies de la communication le 2 août 2021 puis confirmé le 11 octobre de la même année comme ministre dans le gouvernement dirigé par Najla Bouden puis par Ahmed Hachani"
    
import redis
import json

REDIS_HOST = 'redis'
DATAFILE = "/data/weather_3000.json"

def get_city_and_main(json_str: str) -> dict:
    """
    Function to get the city and the weather information as a tuple
    """
    json_dict = json.loads(json_str)
    return json_dict['city']['findname'], json_dict['main']

r = redis.Redis(REDIS_HOST)
with open(DATAFILE, 'r') as f:
    for json_str in f:
        city, main = get_city_and_main(json_str)
        r.mset({city: str(main)})

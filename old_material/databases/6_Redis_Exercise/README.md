# Redis Exercise

In this module we will create a containerized python application that can read weather data and insert it in a redis instance. 

The data file is the same as before:
```
../data/weather_3000.json
```

Your objective is to change the code in `app/app.py` to put the data from this file into our redis instance. 

Redis won't accept a `dict` object, so you have to put convert it to string first.

## Building your project

```
# Building the images
docker-compose build

# Running the containers
docker-compose up
```

## Testing the output

Use the `redis-cli` to validate your outputs

```
docker exec -it 6_redis_exercise_redis_1 redis-cli
```

```
127.0.0.1:6379> GET default
"{'msg': 'Hello World from Redis'}"
```

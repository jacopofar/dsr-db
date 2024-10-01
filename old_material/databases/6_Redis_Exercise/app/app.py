import redis


REDIS_HOST = 'redis'

r = redis.Redis(REDIS_HOST)

payload = {"msg": "Hello World from Redis"}

r.mset({"default": str(payload)})
print(r.get("default"))


import os
import redis
import json

redis_conn = redis.Redis(charset="utf-8", decode_responses=True)

def pub():
    data = {
        "message": "hello",
        "from": "Netra",
        "to": "YOUR_NUMBER"
    }
    redis_conn.publish("broadcast", json.dumps(data))

if __name__ == "__main__":
    pub()
import os
import redis
import json


from multiprocessing import Process

redis_conn = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def sub(name: str):
    pubsub = redis_conn.pubsub()
    pubsub.subscribe("broadcast")
    for message in pubsub.listen():
        if message.get("type") == "message":
            data = json.loads(message.get("data"))
            print("%s : %s" % (name, data))

           
            body = data.get("message")
            from_ = data.get("from")
            to = data.get("to")

            print("Body " + body)
            print("from " + from_)
            print("to : "+ to)


if __name__ == "__main__":
    Process(target=sub, args=("reader1",)).start()

print("Netra")
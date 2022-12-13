import redis
from dotenv import load_dotenv
import os

load_dotenv()

class Redis :
    def __init__(self):
        self.r = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv("REDIS_PORT"), db=os.getenv("REDIS_DB"))
        self.p = self.r.pubsub()

        self.p.subscribe(os.getenv('REDIS_CHANNEL'))

    def listen(self):
        return self.p.listen()
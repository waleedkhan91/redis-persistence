import redis
import time
from datetime import datetime
# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = "redis-pers-test3"
redis_port = 6379
redis_password = ""
def hello_redis(name, key):
  """Example Hello Redis Program"""
  # step 3: create the Redis Connection object
  try:
    # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
    # using the default encoding utf-8. This is client specific.
    r = redis.Redis(host=redis_host, port=redis_port, db=0, socket_timeout=2)
    # step 4: Set the hello message in Redis
    r.set(str(name), str(key), 60)
    # step 5: Retrieve the hello message from Redis
    msg = r.get(name)
    print(str(name) + ' : ' + str(msg))
  except Exception as e:
    print(e)
if __name__ == '__main__':
  while True :
    time.sleep(2.0)
    hello_redis(str(datetime.now().strftime('%d')) + '-' +str(datetime.now().strftime('%S')) + '-' + str(datetime.now().microsecond), 'this is key' )

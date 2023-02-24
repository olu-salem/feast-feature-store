import redis

host = 'localhost'
port = 6379
client = redis.Redis(host=host, port=port)

print(client.ping())

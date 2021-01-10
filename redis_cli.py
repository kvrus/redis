import redis

try:
    conn = redis.StrictRedis(
        host='192.168.56.222',
        port=6379)
    print conn
    conn.ping()
    print 'Connected!'
except Exception as ex:
    print 'Error:', ex
    exit('Failed to connect, terminating.')
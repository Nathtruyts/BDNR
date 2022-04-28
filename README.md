# BDNR
import redis

conR = redis.Redis(
    host='redis-16522.c299.asia-northeast1-1.gce.cloud.redislabs.com',
    port=16522,
    password='Eva02')

conR.set('user:name','shinji')

print(conR.get('user:name'))

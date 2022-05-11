import redis

r = redis.Redis(
    host='redis-10018.c299.asia-northeast1-1.gce.cloud.redislabs.com:10018',
    port="10018", 
    password='nerve1')

r.set('user:name','Nome;heat30', 'Valor:30,00')

print(r.get('cupom:1'))

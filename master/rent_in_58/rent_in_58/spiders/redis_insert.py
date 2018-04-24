import redis


def url_insert_1(url):
    db = redis.Redis(host='127.0.0.1', port=6379, db=0, password='1992825')
    db.lpush('list_url', url)


def url_insert_2(url):
    db = redis.Redis(host='127.0.0.1', port=6379, db=0, password='1992825')
    db.lpush('detail_url', url)


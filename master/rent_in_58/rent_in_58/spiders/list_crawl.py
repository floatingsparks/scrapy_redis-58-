from scrapy_redis.spiders import RedisSpider
from rent_in_58.items import RentIn58Item
from rent_in_58.spiders.redis_insert import url_insert_1, url_insert_2

class RentList(RedisSpider):
    name = 'rent_58'
    redis_key = 'list_url'

    def parse(self, response):
        # data = response.xpath('//*[@id="post-7"]/div[1]/div[1]/div/ul/li[1]/h3/text()').extract()
        # print(data)
        data = response.xpath('//ul[@class="listUl"]/li/@logr').extract()
        for single_one in data:
            one_id = single_one.split('_')[3]
            detail_url = 'http://sz.58.com/zufang/' + str(one_id) + 'x.shtml'
            url_insert_2(detail_url)
        page = response.xpath('//*[@id="bottom_ad_li"]/div[2]/strong/span/text()').extract()[0]
        if int(page) < 70:
            a = int(page) + 1
            list_url = 'http://sz.58.com/chuzu/pn{}'.format(str(a))
            url_insert_1(list_url)
            print('success')
        if int(page) == 70:
            return

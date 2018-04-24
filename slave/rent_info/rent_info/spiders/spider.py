from scrapy_redis.spiders import RedisSpider
from rent_info.items import RentInfoItem
import re
import time
class RentInfo(RedisSpider):
    name = 'rent_info'
    redis_key = 'detail_url'
    #页面无效的处理？
    def parse(self, response):
        #try:
            item = RentInfoItem()
            item['url'] = re.findall('^http\:\/\/\w+\.58\.com\/\w+\/\d+x.shtml', response.url)
            try:
                posttime = response.xpath('//div[@class="house-title"]/p/text()').extract()[0].split()[0]
                TIMEFORMAT = '%Y-%m-%d %X'
                a = time.localtime()
                time_crawl = time.strftime(TIMEFORMAT, a)
                item['time'] = {'time_post': posttime, 'time_crawl': time_crawl}
            except:
                TIMEFORMAT = '%Y-%m-%d %X'
                a = time.localtime()
                time_crawl = time.strftime(TIMEFORMAT, a)
                item['time'] = { 'time_crawl': time_crawl}
            try:
                item['title'] = response.xpath('/html/body/div[4]/div[1]/h1/text()').extract()
            except:
                item['title'] = '抓取错误'
            item['price'] = response.xpath('//div[@class="house-basic-info"]/div[2]/div[1]/div[1]/div/span[1]/b/text()').extract()
            item['rent_style'] = response.xpath('//div[@class="house-basic-info"]/div[2]/div[1]/div[1]/ul/li[1]/span[2]/text()').extract()
            try:
                item['house_style'] = list(response.xpath('//div[@class="house-basic-info"]/div[2]/div[1]/div[1]/ul/li[2]/span[2]/text()').extract())[0].split()
            except:
                item['house_style'] = '抓取错误'
            item['community'] = response.xpath('/ html / body / div[4] / div[2] / div[2] / div[1] / div[1] / ul / li[4] / span[2] / a/text()').extract()
            try:
                a = response.xpath('//div[@class="house-basic-info"]/div[2]/div[1]/div[1]/ul/li[5]')
                b = a.xpath('string(.)').extract()[0]
                item['region'] = re.sub(' +', ' ', b).split()
            except:
                item['region'] = '抓取错误'
            try:
                item['location'] = response.xpath('//div[@class="house-basic-info"]/div[2]/div[1]/div[1]/ul/li[6]/span[2]/text()').extract()[0].split()
            except:
                item['location'] = '深圳'
            item['landlord'] = response.xpath('////*[@id="bigCustomer"]/p[1]/a/text()').extract()
            item['phone'] = response.xpath('//div[@class="house-chat-phone"]/span/text()').extract()
            try:
                c = response.xpath('//ul[@class="introduce-item"]')
                d = c.xpath('string(.)').extract()[0]
                item['description'] = d.split()
            except:
                item['description'] = '抓取错误'
            print('解析成功')
            yield (item)
        
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RentInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    rent_style = scrapy.Field()
    house_style = scrapy.Field()
    community = scrapy.Field()
    region = scrapy.Field()
    location = scrapy.Field()
    landlord = scrapy.Field()
    phone = scrapy.Field()
    description = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompscrapyAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    prof_title = scrapy.Field()
    degrees = scrapy.Field()
    research_interests = scrapy.Field()
    homepage = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    fax = scrapy.Field()
    office = scrapy.Field()
    by_mail_or_courier = scrapy.Field()
    #title = scrapy.Field()
    pass

#!/Users/Kelvin/python-virtual-envs/compscienv/bin/python

# File:    eventsspider.py
# Author:  Kelvin Lawson
# Date:    July 8, 2018
# Version: 1.0
#
# Purpose: To crawl the CS news and events page and extract the data 
#          from the upcoming events link


# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EventsspiderSpider(CrawlSpider):
    name = 'eventsspider'
    allowed_domains = ['cs.acadiau.ca']
    start_urls = ['https://cs.acadiau.ca/news-events.html']

    rules = (
        Rule(LinkExtractor(allow=('/news-events.html', )), 
            process_links='filter_link', follow=True),
    )


    def filter_link(self, links):
        for link in links:
            if '?' in link.url:
                continue
            else:
                yield link

    
    def parse(self, response):
        for href in response.css('div.event.layout_upcoming.upcoming.even.first.last.cal_202 a::attr(href)'):
            yield response.follow(href, self.parse_item)


    def parse_item(self, response):
        i = {}

        title_list = response.xpath('//*[@id="event-items-15421"]/div[2]/div/h1/text()').extract()
        data_list = response.xpath('//*[@id="event-items-15421"]/div[2]/div/div[1]/p/span/text()[not (contains(., "\xa0"))]').extract()

        for x in range(0, len(title_list)):
            i['title'] = title_list[x]

            for data in data_list:
               i['data'] = data_list

            i['data'] = ' '.join(i['data'])

            yield i

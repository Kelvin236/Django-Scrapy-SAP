# File:    csScraper.py
# Author:  Kelvin Lawson
# Date:    June 10, 2018
# Version: 1.0
#
# Purpose: To crawl the computer science faculty and staff page and extract
#          faculty/staff profile information


# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from compScrapy_app.items import CompscrapyAppItem


class CsscraperSpider(CrawlSpider):
    name = 'csScraper'

    # Name:    __init__
    # Purpose: A spider constructor that receives arguments from Django

    #def __init__(self, *args, **kwargs):
        #self.domain = kwargs.get('domain')
        #self.url = kwargs.get('url')

        #self.allowed_domains = [self.domain]
        #self.start_urls = [self.url]

        #CsscraperSpider.rules = [
            #Rule(LinkExtractor(unique=True), callback='parse_item'),
        #]
        #super(CsscraperSpider, self).__init__(*args, **kwargs)
        
    # Attributes that create the initial requests for the spider 
    allowed_domains = ['cs.acadiau.ca']

    # start_url for upcoming seminar will have to be changed to its url
    # when it is uplpaded to the CS website
    start_urls = ['https://cs.acadiau.ca/people/facultystaff/klawson.html']

    # defines how the spider will follow links in the webpage

    rules = (
        Rule(LinkExtractor(allow=('klawson.html', )), callback='parse_item', follow=True),
    )

    # A callback method to handle each request for the URLs
    # Here, use Scrapy mechanisms (xpath) to select parts of HTML 
    # and extract data from website.
    # Xpath defines selectors to associate styles with specifc HTML
    # elements

    def parse_item(self, response):
        item = {}
        name_list = response.xpath('//*[@class="mod_article first last block"]/div/h2/text()').extract()
        prof_title_list = response.xpath('//*[@class="mod_article first last block"]/div/p[1]/strong/text()').extract()
        degrees_list = [' '.join(degree.xpath('//*[@class="mod_article first last block"]/div/ul[1]/li/text()').extract())
                            for degree in response.xpath('//*[@class="mod_article first last block"]/div')]
        research_list = [' '.join(research.xpath('//*[@class="mod_article first last block"]/div/ul[2]/li/text()').extract())
                            for research in response.xpath('//*[@class="mod_article first last block"]/div')]
        homepage_list = response.xpath('//*[@class="mod_article first last block"]/div/p[6]/a/text()').extract()
        email_list = response.xpath('//*[@class="mod_article first last block"]/div/p[7]/a/text()').extract()
        phone_list = response.xpath('//*[@class="mod_article first last block"]/div/p[7]/text()[2]').extract()
        fax_list = response.xpath('//*[@class="mod_article first last block"]/div/p[7]/text()[3]').extract()
        office_list = response.xpath('//*[@class="mod_article first last block"]/div/p[7]/text()[4]').extract()
        by_mail_or_courier_list = [" ".join(mail.xpath('//*[@class="mod_article first last block"]/div/p[8]/text()').extract())
                                    for mail in response.xpath('//*[@class="mod_article first last block"]/div')]
        for x in range(0, len(name_list)):
            item['name'] = name_list[x]
            item['prof_title'] = prof_title_list[x]
            item['degrees'] = degrees_list[x]
            item['research_interests'] = research_list[x] 
            item['homepage'] = homepage_list[x]
            item['email'] = email_list[x]
            item['phone'] = phone_list[x]
            item['fax'] = fax_list[x]
            item['office'] = office_list[x]
            item['by_mail_or_courier'] = by_mail_or_courier_list[x]
            yield item

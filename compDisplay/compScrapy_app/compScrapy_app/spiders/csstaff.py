# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from compScrapy_app.items import CompscrapyAppItem


class CsstaffSpider(CrawlSpider):
    name = 'csstaff'
    allowed_domains = ['cs.acadiau.ca']
    # start_urls = [
    #     'https://cs.acadiau.ca/swatson.html',
    #     'https://cs.acadiau.ca/gwalsh.html',
    #     'https://cs.acadiau.ca/people/facultystaff/jfindley.html',
    #     'https://cs.acadiau.ca/people/facultystaff/htravers.html',
    #     'https://cs.acadiau.ca/fabdelmohsen.html',
    #     'https://cs.acadiau.ca/jwalsh.html',
    #     'https://cs.acadiau.ca/mMain.html',
    #     'https://cs.acadiau.ca/sYang.html',
    #     'https://cs.acadiau.ca/bHe.html',
    #     'https://cs.acadiau.ca/people/facultystaff/klawson.html'
    # ]

    # rules = (
    #     Rule(LinkExtractor(allow=('klawson.html', )), callback='parse_item', follow=True),
    # )

    start_urls = ['https://cs.acadiau.ca']

    rules = (
        Rule(LinkExtractor(allow=('facultystaff.html', ), 
                            deny=('computer-science-degree-programs.html', 
                                  'news-events.html', 
                                  'videos.html', 
                                  'prospective-students.html', 
                                  'degree-programs-7145.html', 
                                  'graduate.html', 
                                  'research-groups.html', 
                                  'career-information.html', 
                                  'outreach.html', 
                                  'contact-us.html',
                                  'dbenoit.html',
                                  'jdiamond.html',
                                  'eshakshuki.html',
                                  'dsilver.html',
                                  'atrudel.html',
                                  'hzhang.html',
                                  'ctrudel.html',
                                  'tmuldner.html',
                                  'jread.html',
                                  'dcurrie.html',
                                  'loliver.html',
                                  'itomek.html'),), follow=True),
    )


    def parse(self, response):
        for href in response.css('li.sibling a::attr(href)'):
            yield response.follow(href, self.parse)
        
        for href in response.css('div.faculty a::attr(href)'):
            yield response.follow(href, self.parse_item)


    def parse_item(self, response):
        i = {}

        employee_list = response.xpath('//*[@class="mod_article first last block"]/div/h2/text()').extract()
        position_list = response.xpath('//*[@class="mod_article first last block"]/div/p[1]/strong/text()').extract()
        employee_email = response.xpath('//*[@class="mod_article first last block"]/div/p[5]/a/text()').extract()
        employee_phone = response.xpath('//*[@class="mod_article first last block"]/div/p[5]/text()[2]').extract()
        employee_fax = response.xpath('//*[@class="mod_article first last block"]/div/p[5]/text()[3]').extract()
        employee_office = response.xpath('//*[@class="mod_article first last block"]/div/p[5]/text()[4]').extract()
        employee_mail = [' '.join(mails.xpath('//*[@class="mod_article first last block"]/div/p[6]/text()').extract())
                                for mails in response.xpath('//*[@class="mod_article first last block"]/div')]
        
        for x in range(0, len(employee_list)):
            i['employee_name'] = employee_list[x]
            i['position'] = position_list[x]
            i['email_addr'] = employee_email[x]
            i['phone_num'] = employee_phone[x]
            i['fax_num'] = employee_fax[x]
            i['office_num'] = employee_office[x]
            i['mail'] = employee_mail[x]
            yield i

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i

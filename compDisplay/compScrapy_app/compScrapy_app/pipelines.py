# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# File:    pipelines.py
# Author:  Kelvin Lawson
# Date:    June 25, 2018
# Version: 1.0
# 
# Purpose: To transmit the extracted data to django models

import json
from compDashboard.models import ProfProfile
#from compDashboard.models import SupportStaff
#from compDashboard.models import ScrapyItem
from scrapy.exceptions import DropItem


class CompscrapyAppPipeline(object):

    # Name:        __init__
    # Purpose:     Constructor for the class.
    # Arguments:  
    # Output:      None
    # Modifies:    None
    # Returns:     None
    # Assumptions: None
    # Bugs:        None
    # Notes:       - self parameter refers to an instance of the object
    #              - this method gets called when memory for the object gets
    #                allocated
    #              - setting the varaibles inside this method as self makes
    #                them persist with the values of the object and accessible
    #                throughout the lifetime of the object

    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        #self.items = []


    # Name:        from_crawler
    # Purpose:     To create a new instance of a pipeline.
    # Arguments:
    # Output:      None
    # Modifies:    None
    # Returns:     An instance of a new pipeline.
    # Assumptions: None
    # Bugs:        None
    # Notes:       - classmethod is a method that belongs to the SQLlitePipeline
    #              - the cls is the SQLlitePipeline class itself

    @classmethod
    def from_crawler(cls, crawler):
        return cls (
            unique_id = crawler.settings.get('unique_id'),
        )

    # Name:        process_item
    # Purpose:     To save the extracted data to the respective columns
    #              of the Django models
    # Arguments: 
    # Output:      None
    # Modifies:    None
    # Returns:     The extracted data 
    # Assumptions: None
    # Bugs:        None
    # Notes:       None

    def process_item(self, item, spider):
        profile = ProfProfile()
        profile.name = item["name"]
        profile.prof_title = item["prof_title"]
        profile.degrees = item["degrees"]
        profile.research_interests = item["research_interests"]
        profile.homepage = item["homepage"]
        profile.email = item["email"]
        profile.phone = item["phone"]
        profile.fax = item["fax"]
        profile.office = item["office"]
        profile.by_mail_or_courier = item["by_mail_or_courier"]
        profile.save()
        # if spider.name == 'csstaff':
        #     staff = SupportStaff()
        #     staff.employee_name = item["employee_name"]
        #     staff.position = item["position"]
        #     staff.email_addr = item["email_addr"]
        #     staff.phone_num = item["phone_num"]
        #     staff.fax_num = item["fax_num"]
        #     staff.office_num = item["office_num"]
        #     staff.mail = item["mail"]
        #     staff.save()

        #     return item
        # elif spider.name == 'eventsspider':
        #     events = ScrapyItem()
        #     events.title = item["title"]
        #     events.data = item["data"]

        #     if events.title and events.data:
        #         if ScrapyItem.objects.filter(title=item["title"]).exists():
        #             raise DropItem("Event is already in Db.")
        #         else:
        #             events.save()

        #     return item

        return item
# File:    models.py
# Author:  Kelvin Lawson
# Date:    May 5, 2018
# Version: 1.0
#
# Purpose: To define the database models (tables) in which the extracted data
#          will be stored.

import json
from django.db import models
from django.utils import timezone

# class ScrapyItem defines the model; it is an object
# The ScrapyItem model represents CS events such as seminars and LAN parties

class ScrapyItem(models.Model): 
    title = models.CharField(max_length=200)
    data = models.TextField() # this is the crawled data

    # Obtain a text(string) with an event title
    # This function is a human readable representation of the events model
    # It returns the title of the ScrapyItem (events) object
    def __str__(self):
        return self.title


    def __iter__(self):
        yield 'title', self.title
        yield 'data', self.data


class ProfProfile(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    prof_title = models.CharField(max_length=50, blank=True, null=True)
    degrees = models.CharField(max_length=500, blank=True, null=True)
    research_interests = models.CharField(max_length=500, blank=True, null=True)
    homepage = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    office = models.CharField(max_length=7, blank=True, null=True)
    by_mail_or_courier = models.CharField(max_length=150, blank=True, null=True)


    def __str__(self):
        return self.name


    def __iter__(self):
        yield 'name', self.name
        yield 'prof_title', self.prof_title
        yield 'degrees', self.degrees
        yield 'research_interests', self.research_interests
        yield 'homepage', self.homepage
        yield 'email', self.email
        yield 'phone', self.phone
        yield 'fax', self.fax
        yield 'office', self.office
        yield 'by_mail_or_courier', self.by_mail_or_courier


class SupportStaff(models.Model):
    employee_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    email_addr = models.CharField(max_length=100, blank=True, null=True)
    phone_num = models.CharField(max_length=12, blank=True, null=True)
    fax_num = models.CharField(max_length=12, blank=True, null=True)
    office_num = models.CharField(max_length=7, blank=True, null=True)
    mail = models.CharField(max_length=150, blank=True, null=True)


    def __str__(self):
        return self.employee_name


    def __iter__(self):
        yield 'employee_name', self.employee_name
        yield 'position', self.position
        yield 'email_addr', self.email_addr
        yield 'phone_num', self.phone_num
        yield 'fax_num', self.fax_num
        yield 'office_num', self.office_num
        yield 'mail', self.mail

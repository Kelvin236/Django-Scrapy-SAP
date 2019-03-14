# Django-Scrapy-SAP
This repository contains files of a single page web application created with Django and Scrapy. It was developed as part of my 
co-operative education project to create an application that would grab HTML from the faculty and events pages of Acadia
University's computer science website, store it in a database then make requests to the database from Django views so that
the data can be displayed on a monitor.

For the project to be a true single page application a feature was implemented so that professor profiles and events 
description would appear on the page for a couple minutes then fade out so that new data can be displayed.

This application was made with Django, Scrapy, HTML5 and CSS.

Django - used to fetch the data from the database and return it to the client
  models.py - the database models are created here so that the extracted data can be saved
  
  views.py - iterates through the stored data and returs it to the client so that it is displayed on a screen


Scrapy - used to crawl the computer science website for the desired data and save the extracted data into a database
  spiders:
    csScraper.py - extracts professor profile information
    csstaff.py - extracts the profiles of other faculty memebers
    eventsspider.py - extracts computer science events information 
  
  pipelines.py - transmits the extracted data to the Django database models in a list format
  
  settings.py - connects Scrapy to Django so that we have access to the database models
  


HTML5 & CSS - used to create the application interface
  templates:
    index.html - sets up the structure of the application interace and includes code that takes care of the desired 
                 fade in / fade out feature
  
  static:
    style.css - takes care of page presentation


At the end of my term there were a few features missing from the application including:
  a cron job that triggers the spider to crawl for new information every couple weeks (this can also be taken care of in
  Django views)
  
  pipelines.py needs to be refactored so that only the specified spider is triggered
  
  a message that appears on the monitor that informs viewers that no new data is available for display whenever this case
  arises


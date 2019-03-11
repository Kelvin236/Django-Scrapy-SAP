# File:    views.py
# Author:  Kelvin Lawson
# Date:    June 7, 2018
# Version: 1.0
#
# Purpose: The purpose of this program is to present the crawled data in a 
#          consistent format. At its core this file will connect the scrapyd
#          application to the spider to trigger crawling. It takes a request
#          from the user, that is, the url to be parsed, and returns the 
#          crawled data. 


#from django.shortcuts import render
#from django.contrib.auth.models import ProfProfile
"""from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from compDashboard.models import ProfProfile
from compDashboard.utils import URLUtil
from scrapyd_api import ScrapydAPI
from uuid import uuid4
from urllib.parse import urlparse """



 # connect to scrapyd service
#scrapyd = ScrapydAPI('http://localhost:6800')

# Name:        validate_given_url
# Purpose:     To check if the url given by the user is valid
# Arguments:   
# Output:      None
# Modifies:    None
# Returns:     True if the given url exists, false if it doesn't exist.
# Assumptions: None
# Bugs:        None
# Notes:       None

""" def validate_url(url):
    validate = URLValidator()
    try:
        validate(url)
    except ValidationError:
        return False
    return True  """


# Name:        crawler
# Purpose:     To schedule the spider to crawl
# Arguments:
# Output:      None
# Modifies:    None
# Returns:     The crawled data  
# Assumptions: None
# Bugs:        None
# Notes:       None

""" @csrf_exempt
@require_http_methods(['POST', 'GET'])
def crawler(request):
    if request.method == 'POST':
        url = request.POST.get('url', None)

        if not url:
            return JsonResponse({'error': 'Missing args'})

        if not validate_url(url):
            return JsonResponse({'error': 'URL is invalid'})

        domain = urlparse(url).netloc
        unique_id = str(uuid4())

        settings = {
            'unique_id': unique_id,
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }

        task = scrapyd.schedule('default', 'csScraper', 
            settings=settings, url=url, domain=domain)
        
        return JsonResponse({'task_id': task, 'unique_id': unique_id, 'status': 'started'})
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        unique_id = request.GET.get('unique_id', None)

        if not task_id or not unique_id:
            return JsonResponse({'error': 'Arguments missing.'})

        status = scrapyd.job_status('default', task_id)

        if status == 'finished':
            try:
                item = ProfProfile.objects.get(unique_id=unique_id)
                return JsonResponse ({
                    'name': item.to_dict['name'],
                    'prof_title': item.to_dict['prof_title'],
                    'degress': item.to_dict['degrees'],
                    'research_interests': item.to_dict['research_interests'],
                    'homepage': item.to_dict['homepage'],
                    'email': item.to_dict['email'],
                    'phone': item.to_dict['phone'],
                    'fax': item.to_dict['fax'],
                    'office': item.to_dict['office'],
                    'by_mail_or_courier': item.to_dict['by_mail_or_courier']
                })
            except Exception as e:
                return JsonResponse({'error': str(e)}) 
        else:
            return JsonResponse({'status': status})  """

    

#Create your views here.
from django.shortcuts import render
from compDashboard.models import ProfProfile, ScrapyItem
from django.http import Http404, HttpResponse
import json

def index(request):
    #prof_info = list(ProfProfile.objects.all())
    #prof_info = ProfProfile.objects.values_list('name', flat=True).order_by('id')
    # prof_info = ProfProfile.objects.values()
    #except ProfProfile.DoesNotExist:
        #pass

    return render(request, 'compDashboard/index.html', {})


def get_events_info_api(request):
    if request.method != 'GET':
        raise Http404()
    
    if request.is_ajax():
        events_info = []
        for e in ScrapyItem.objects.all():
            events_info.append(dict(e))

        return HttpResponse(json.dumps(events_info))
 

def get_prof_info_api(request):
    if request.method != 'GET':
        raise Http404()
        
    if request.is_ajax():
        prof_info = []
        for p in ProfProfile.objects.all():
            prof_info.append(dict(p))

        return HttpResponse(json.dumps(prof_info))


def get_sup_staff_info_api(request):
    if request.method != 'GET':
        raise Http404()
    
    if request.is_ajax():
        staff_info = []
        for s in SupportStaff.objects.all():
            staff_info.append(dict(s))

        return HttpResponse(json.dumps(staff_info))
    
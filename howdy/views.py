 # howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime
from django.http import HttpResponse


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"
# DateTime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"  % now  
    return HttpResponse(html)

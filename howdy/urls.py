# howdy/urls.py
from django.conf.urls import url
from howdy import views
from howdy.views import current_datetime

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), 
    url(r'^time/$', current_datetime),
]
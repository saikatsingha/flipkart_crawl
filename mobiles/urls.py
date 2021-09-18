from django.conf.urls import url
from django.urls import path
from mobiles import views
from . import views

urlpatterns = [
    url(r'', views.mobilesApi),
    # path('', views.mobilesAPI, name='mobiles'),
]

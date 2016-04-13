from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
	url(r'^$', 'studentapp.views.details'),
	url(r'^studentform/show/', 'studentapp.views.show'),

]
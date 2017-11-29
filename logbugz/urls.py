"""logbugz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bugz import views 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home, name = 'home'),                                       # UserLogin
    url(r'bugz/mysummary$',views.bugsummary_admin,name = 'summary_admin' ),     # summary of bugs 
    url(r'bugz/(?P<bug_id>[0-9]+)$',views.bugdetails,name = 'bugdetails' ),     # see bug details
    url(r'bugz/registerbug$',views.registerbug,name = 'registerbug'),           # raise a new bug
    url(r'bugz/thankyou$',views.thankyou, name = 'thankyou'),                   # thanks for using me
]

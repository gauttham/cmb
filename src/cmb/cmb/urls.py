"""cmb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^DedicatedAccounts/$', views.DedicatedAccountList.as_view()),
    url(r'^DedicatedAccounts/(?P<pk>[0-9]+)/$', views.DedicatedAccountDetails.as_view()),
    url(r'^ServiceClasses/$', views.ServiceClassList.as_view()),
    url(r'^ServiceClasses/(?P<pk>[0-9]+)/$', views.ServiceClassDetails.as_view()),
    url(r'^ExceptionList/$', views.ExceptionListList.as_view()),
    url(r'^ExceptionList/(?P<pk>[0-9]+)/$', views.ExceptionListDetails.as_view()),
    url(r'^PrepaidInCdr/$', views.PrepaidInCdrList.as_view()),
    url(r'^PrepaidInCdr/(?P<pk>[0-9]+)/$', views.PrepaidInCdrDetails.as_view()),
    url(r'^DaInCdrMap/$', views.DaInCdrMapList.as_view()),
    url(r'^DaInCdrMap/(?P<pk>[0-9]+)/$', views.DaInCdrMapDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


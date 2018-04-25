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
from rest_framework.documentation import include_docs_urls
from . import csvloader

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='CMB Reconciliation Tool APIs')


urlpatterns = [
    # url(r'^login', views.login),
    url(r'^docs/', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^DedicatedAccounts/$', views.DedicatedAccountList.as_view()),
    url(r'^DedicatedAccounts/(?P<pk>[0-9]+)/$', views.DedicatedAccountDetails.as_view()),
    url(r'^ServiceClasses/$', views.ServiceClassList.as_view()),
    url(r'^ServiceClasses/(?P<pk>[0-9]+)/$', views.ServiceClassDetails.as_view()),
    url(r'^ExceptionList/$', views.ExceptionListList.as_view()),
    url(r'^ExceptionList/(?P<pk>[0-9]+)/$', views.ExceptionListDetails.as_view()),
    url(r'^PrepaidInCdr/$', views.InCdrList.as_view()),
    url(r'^PrepaidInCdr/(?P<pk>[0-9a-zA-Z]+)/$', views.InCdrDetails.as_view()),
    url(r'^DaInCdrMap/$', views.DaInCdrMapList.as_view()),
    url(r'^DaInCdrMap/(?P<pk>[0-9]+)/$', views.DaInCdrMapDetails.as_view()),
    url(r'^beepCDR/$', views.BeepCDRList.as_view()),
    url(r'^beepCDR/(?P<pk>[0-9]+)/$', views.BeepCDRDetails.as_view()),
    url(r'^RevenueConfig/$', views.RevenueConfigList.as_view()),
    url(r'^RevenueConfig/(?P<pk>[0-9]+)/$', views.RevenueConfigDetails.as_view()),
    url(r'^Freebies/$', views.FreebiesList.as_view()),
    url(r'^Freebies/(?P<pk>[0-9]+)/$', views.FreebiesDetails.as_view()),
    url(r'^FreebiesType/$', views.FreebiesTypeList.as_view()),
    url(r'^FreebiesType/(?P<pk>[0-9]+)/$', views.FreebiesTypeDetails.as_view()),
    url(r'^BulkLoader/$', views.BulkLoader.as_view()),
    # url(r'^BulkLoader/$', views.samplepost),
    # url(r'^sample/$', views.DAViewSet.as_view()),
    url(r'^dacsv/$', csvloader.DAViewSet.as_view()),
    url(r'^reports/report1', views.Report1.as_view()),
    url(r'^reports/revenueReport', views.RevenueReport.as_view()),
    url(r'^reports/nonRevenueReport', views.NoNRevenueReport.as_view()),
    url(r'^reports/stats1', views.Stats1.as_view()),
    url(r'^execute/revenue', views.ExecuteRevenueCalculator.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'csv'])


"""hiren URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from reminder import views
from django.contrib.auth.views import logout
from api import urls as api

urlpatterns = [
    url(r'^$', views.index, name='login'),
    url(r'^api/', include(api)),
    url(r'^create/', views.create, name='create'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^reminder/(?P<pk>\d+)/$', views.reminder, name='reminder'),
    url(r'^reminder/(?P<pk>\d+)/update/', views.reminder_update, name='reminder_update'),
    url(r'^reminders/', views.reminders, name='reminders'),
    url(r'^archives/', views.archived, name='archives'),
    url(r'^active/', views.active, name='active'),
    url(r'^jobs/', views.job),
    url(r'^logout/', logout, {'next_page': '/'}, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]


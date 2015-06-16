__author__ = 'prism'
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, ReminderViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reminder', ReminderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
]


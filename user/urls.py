# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'user', UserViewSet)
router.register(r'history', HistoryViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('login', Authentication.login),
    path('signup', Authentication.signup),
    path('test_token', Authentication.test_token),
    path('view_history', HistoryQuery.view),
    path('cal_fee', HistoryQuery.late_fee),
    path('borrow', HistoryQuery.borrow),
]

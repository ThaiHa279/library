# basic URL Configurations
from django.urls import include, path, re_path
# import routers
from rest_framework import routers

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'user', UserViewSet)
router.register(r'book', BookViewSet)
router.register(r'book-genres', BookGenresViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('login', Authentication.login),
    path('signup', Authentication.signup),
    path('test_token', Authentication.test_token),
]

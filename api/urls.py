from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
    # path('', views.home, name='blog-home'),
    path('registration/', include('rest_auth.registration.urls')),
]

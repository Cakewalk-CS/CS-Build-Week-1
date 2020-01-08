from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
<<<<<<< HEAD
    url('rooms', api.rooms),
=======
    url('rooms', api.rooms)
>>>>>>> b8377438443f94d43db8b8e3eb255e0f91cf9a0e
]
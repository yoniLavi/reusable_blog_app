from django.conf.urls import url
from . import views


urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.post_list, name='blog'),
=======
    url(r'^$', views.post_list name='blog'),
>>>>>>> 379a9997657d76199cded1ed3c1ce1ccecedc4e1
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^top', views.top_five),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name='edit'),
]

from django.urls import re_path
from . import views

urlpatterns = [
    # post views
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]

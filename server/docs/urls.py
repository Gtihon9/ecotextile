from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.docs_list, name='docs_list'),
    re_path(r'^(?P<pk>[-\w]+)/$',
        views.doc_view,
        name='doc_view'),
]

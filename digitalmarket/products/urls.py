from django.conf.urls import include, url
from .views import detail_view, list_view, detail_slug_view, create_view

urlpatterns = [
    url('create/$', create_view, name='create_view'),
    url('detail/(?P<object_id>\d+)/$', detail_view, name='detail_view'),
    url('detail/(?P<slug>[\w-]+)/$', detail_slug_view, name='detail_slug_view'),
    url('list/$', list_view, name='list_view'),
]
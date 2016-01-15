from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='movie.index'),
    url(r'^mv/(\d+)/$', views.post, name="movie.post"),
]

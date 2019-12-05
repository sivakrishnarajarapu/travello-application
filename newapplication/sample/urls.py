from django.conf.urls import url
from sample import views

urlpatterns = [
    # url('', views.index, name='index'),
    url('add', views.add, name='add'),
]

from django.conf.urls import url

from travello import views


urlpatterns = [
    url('',views.index,name='index'),
]

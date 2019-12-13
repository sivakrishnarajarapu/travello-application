from django.conf.urls import url

from accounts import views


urlpatterns = [
    url('register', views.register, name='register'),
    url('login', views.login, name='login'),
    url('logout', views.logout, name='logout')
]

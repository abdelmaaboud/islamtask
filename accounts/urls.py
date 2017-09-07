from django.conf.urls import url
from django.contrib.auth.views import logout

from django.conf import settings
from accounts import views

urlpatterns = [

    url(r'^$', views.login_and_register),
    url(r'^register/', views.login_and_register),
    url(r'^login/', views.login_and_register),

    url(r'^login_/', views.check_login),
    url(r'^regist/', views.check_register),
    url(r'^logout/',logout, {'next_page': '/accounts/'}),
    url(r'^welcome/',views.welcome),
    url(r'^profile/',views.get_profile),
    url(r'^upload/', views.model_form_upload),


]
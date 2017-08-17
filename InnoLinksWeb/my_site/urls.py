from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response

from . import views

urlpatterns = [
    url(r'^main/', views.form_main),
    url(r'^logout/', views.logout_site),
    url(r'^/logout/', views.logout_site),

    url(r'^', views.login),

]

"""WebFWProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from myapp import views
from .views import MyAppView

urlpatterns = [
    # Different formats of URLs
    path('show/', views.show),
    path('show_count/<int:count>', views.show_count, name='count'),
    re_path(r'show_year/(?P<year>[0-9]{4})$', views.show_year),

    # Templates
    path('show_template/', views.show_template, name='shw_tpl'),
    path('template_var_demo/', views.template_var_demo),
    path('template_if_tag_demo/', views.template_if_tag_demo),
    path('template_for_tag_demo/', views.template_for_tag_demo),
    path('template_empty_for_tag_demo/', views.template_empty_for_tag_demo),
    path('template_cycle_tag_demo/', views.template_cycle_tag_demo),
    path('template_inheritance_demo/', views.template_inheritance_demo),
    path('template_comments_demo/', views.template_comments_demo),

    # Class based views
    path('class_based/show_template/', MyAppView.as_view(), name='show_template'),

    # Redirect demo
    path(
        'temporary_page_redirect_url/',
        views.temporary_page_redirect_url
    ),
    path(
        'temporary_page_redirect_name/',
        views.temporary_page_redirect_name,
        name='temp_redirect_name'
    ),
    path(
        'redirect_path_parameters/',
        views.redirect_path_parameters,
        name='redirect_path_parameters'
    ),
    path(
        'permanent_page_redirect/',
        views.permanent_page_redirect
    )
]

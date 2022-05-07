from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from .views import home, post_create, form_create, not_hesapla #form_create #kendi app dizinimde oluşturduğum vieweler


urlpatterns = [
    re_path(r'^$', view=post_create),
    re_path(r'^home/$', view=home),
    re_path(r'^form/$', view=form_create),
    re_path(r'^not/$', view=not_hesapla),
    #path('', post_list ),
    #path('', post_update ),
    #path('', post_create ),
]
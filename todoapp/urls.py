from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.home),
    re_path(r"^delete/(?P<key>\w+)/$", views.delete),
    re_path(r"^edit/(?P<key>\w+)/$", views.edit),
    re_path(r"^view/(?P<key>\w+)/$", views.get_one), 
    path('view', views.get_all)
]

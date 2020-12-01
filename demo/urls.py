from django.urls import path

from demo.views import Index

urlpatterns = [
    path('' , Index.as_view() , name = 'home'),
]
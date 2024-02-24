from django.urls import path
from .views import *
app_name='unique'

urlpatterns=[

    path('specific1/',specific1,name='specific1'),
    path('specific2/',specific2,name='specific2'),
]

from django.contrib import admin
from django.urls import path,include
from basic import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.showdata,name='data')
]

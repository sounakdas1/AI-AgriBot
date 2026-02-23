
from django.contrib import admin
from django.urls import path,include
from basic import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',v.showdata,name='data'),
    path('set-command/',v.set_command,name='set_data'),
    path('upload/',v.upload_image,name='upload_data')
]

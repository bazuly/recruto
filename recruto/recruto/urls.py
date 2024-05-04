from django.contrib import admin
from django.urls import path, include
from hello_recruto.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello_recruto.urls'), name='hello_recruto')
]

from django.urls import path
from .views import index

app_name = 'hello_recruto'

urlpatterns = [
    path('hello_recruto/Recruto&message/ДавайДружить', index, name='recruto-message')
]

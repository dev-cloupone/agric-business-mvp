from django.urls import path
from . import views

app_name = 'fields'

urlpatterns = [
    path('import-fields/', views.import_fields, name='import_fields'),
    path('get/', views.get, name='get')
]
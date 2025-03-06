from django.urls import path
from . import views
    
urlpatterns=[
    path('',views.form_display,name="form display")
    
]


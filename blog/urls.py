from django.urls import path
from . import views
    
urlpatterns=[
    path('',views.form_display,name="form display"),
    path("listview/",views.Articleclass_view.as_view(),name="list_view"),
    path("<int:id>/",views.Detailclassview.as_view(),name="detailview"),
    
]


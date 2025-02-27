from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_page,name="homepage"),
    path("about/",views.about,name="aboutpage"),
    path("model_data/",views.data_from_model,name="data rendering"),
    path("create/",views.enterdata,name="data saving")
]


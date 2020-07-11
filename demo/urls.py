from django.urls import path
from . import views 

# /posts
urlpatterns = [
    
    #path('search/',views.UsersearchtView.as_view(),name="search"),
    path('list/', views.HospitalList),
    path('data/', views.my_custom_sql),
    #path('detail/<int:pk>/', views.HospitalDetail.as_view()),
]
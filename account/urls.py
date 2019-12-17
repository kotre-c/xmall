from django.urls import path
from account import views

urlpatterns = [
    path('<username>', views.UserListView.as_view()),
    path('image/<username>/', views.UserImgView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('', views.UserRegistView.as_view()),
]

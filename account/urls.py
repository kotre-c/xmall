from django.urls import path
from account import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<username>', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
]

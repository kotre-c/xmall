from django.urls import path
from account import views

urlpatterns = [
    path('<username>', views.UserListView.as_view()),
    # path('detail/<pk>/', views.GoodDetailView.as_view())
]

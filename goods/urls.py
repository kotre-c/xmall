from django.urls import path
from goods import views

urlpatterns = [
    path('', views.GoodListView.as_view()),
    path('<int:pk>/', views.GoodDetailView.as_view())
]

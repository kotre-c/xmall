from django.urls import path
from address import views

urlpatterns = [
    path('', views.AddressListView.as_view()),
    path('<int:pk>/', views.AddressDetailView.as_view()),

]
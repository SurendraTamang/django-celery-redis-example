from django.urls import path,include
from invitation import views

urlpatterns = [
    path('', views.SignUpView.as_view(),name="signup"),
    path('/success/', views.SuccessView.as_view(),name="success")
]
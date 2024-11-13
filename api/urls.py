from django.urls import path
from . import views
from .views import ListTodo,DeleteTodo,DetailTodo,CreateTodo,RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns =[
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('delete/<int:pk>/', DeleteTodo.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token

]
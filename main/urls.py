from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from main.views import *

urlpatterns = [
    # TODOs
    path('todos/', get_todo_list, name='todo_list'),
    path('todos/<id>/completed/', get_completed_todo_list, name='completed_todo_list'),

    # APIs
    path('api/todos/', TaskListAPIView.as_view(), name='api_todo_list'),
    path('api/todos/<id>/completed/', TaskDetailAPIView.as_view(), name='api_completed_todo_list'),

    # JWT
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

]

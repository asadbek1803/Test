from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/status/', views.TaskUpdateStatusView.as_view(), name='update_status'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('api/', views.TaskListAPI.as_view(), name='api'),
]

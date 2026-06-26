from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('create/', views.EmployeeCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.EmployeeEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='delete'),
    path('api/', views.EmployeeListAPI.as_view(), name='api'),
]

from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apiOverview, name='api-overview'),
    #path('task-list/', views.taskList, name='task-list'),
    #path('task-detail/<str:pk>/', views.taskDetail, name='task-detail'),
    #path('task-create/', views.taskCreate, name='task-create'),
    #path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    #path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),
    path('', views.StatusAPIView.as_view(), name='api-overview'),
    path('<str:pk>/', views.StatusDetailAPIView.as_view(), name='task-detail'),
    
]
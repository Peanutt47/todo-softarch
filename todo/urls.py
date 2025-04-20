from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='todo_list'),
    path('add/', views.todo_views.add_todo, name='add_todo'),
    path('update/<int:pk>/', views.todo_views.update_todo, name='update_todo'),
    path('delete/<int:pk>/', views.todo_views.delete_todo, name='delete_todo'),
]
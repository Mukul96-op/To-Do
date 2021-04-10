from django.urls import path
from tasks.views import home , updateTask ,deleteTask

urlpatterns = [
	path('', home, name="list"),
	path('update_task/<str:pk>/', updateTask, name="update_task"),
	path('delete/<str:pk>/', deleteTask, name="delete"),
]
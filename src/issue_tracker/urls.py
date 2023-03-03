from django.urls import path

from .views import IndexView
from .views import TaskDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', IndexView.as_view(), name='tasks'),
    path('tasks/task/<int:pk>', TaskDetailView.as_view(), name='task_detail')
]

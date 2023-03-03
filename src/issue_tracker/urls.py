from django.urls import path

from .views import IndexView
from .views import TaskDetailView
from .views import TaskAddView
from .views import TaskEditView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/', IndexView.as_view(), name='tasks'),
    path('tasks/task/create/', TaskAddView.as_view(), name='task_create'),
    path('tasks/task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/task/edit/<int:pk>', TaskEditView.as_view(), name='task_update'),

]

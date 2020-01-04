from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("category", api.categoryViewSet)
router.register("task", api.taskViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("task/category/", views.categoryListView.as_view(), name="task_category_list"),
    path("task/category/create/", views.categoryCreateView.as_view(), name="task_category_create"),
    path("task/category/detail/<int:pk>/", views.categoryDetailView.as_view(), name="task_category_detail"),
    path("task/category/update/<int:pk>/", views.categoryUpdateView.as_view(), name="task_category_update"),
    path("task/task/", views.taskListView.as_view(), name="task_task_list"),
    path("task/task/create/", views.taskCreateView.as_view(), name="task_task_create"),
    path("task/task/detail/<int:pk>/", views.taskDetailView.as_view(), name="task_task_detail"),
    path("task/task/update/<int:pk>/", views.taskUpdateView.as_view(), name="task_task_update"),
)

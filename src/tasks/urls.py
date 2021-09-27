from rest_framework import routers

from tasks.api import views


app_name = 'tasks'

router = routers.DefaultRouter()
router.register('projects', views.ProjectsViewSet)

urlpatterns = []

urlpatterns += router.urls

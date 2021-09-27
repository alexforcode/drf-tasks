from rest_framework import viewsets

from tasks.models import Project
from tasks.api import serializers
from tasks.api.permissions import ProjectsPermission


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = (ProjectsPermission,)

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create']:
            return serializers.ProjectDetailSerializer

        return serializers.ProjectSerializer

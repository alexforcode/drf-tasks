from rest_framework import serializers

from tasks.models import Project


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'user': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        project = Project.objects.create(**validated_data)
        project.save()

        return project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description')

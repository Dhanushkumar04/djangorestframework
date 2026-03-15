from rest_framework import serializers
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificationMapping
        fields = ['id', 'course', 'certification', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        course = data.get('course')
        primary_mapping = data.get('primary_mapping', False)

        mapping_id = self.instance.id if self.instance else None

        if primary_mapping:
            qs = CourseCertificationMapping.objects.filter(course=course, primary_mapping=True)
            if mapping_id:
                qs = qs.exclude(id=mapping_id)
            if qs.exists():
                raise serializers.ValidationError("This course already has a primary certification mapping.")

        return data

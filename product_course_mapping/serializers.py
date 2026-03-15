from rest_framework import serializers
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCourseMapping
        fields = ['id', 'product', 'course', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        product = data.get('product')
        primary_mapping = data.get('primary_mapping', False)

        mapping_id = self.instance.id if self.instance else None

        if primary_mapping:
            qs = ProductCourseMapping.objects.filter(product=product, primary_mapping=True)
            if mapping_id:
                qs = qs.exclude(id=mapping_id)
            if qs.exists():
                raise serializers.ValidationError("This product already has a primary course mapping.")

        return data

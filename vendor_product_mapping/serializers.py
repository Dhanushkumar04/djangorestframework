from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProductMapping
        fields = ['id', 'vendor', 'product', 'primary_mapping', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        vendor = data.get('vendor')
        primary_mapping = data.get('primary_mapping', False)

        # Handle updates (self.instance is not None)
        mapping_id = self.instance.id if self.instance else None

        # Primary Mapping Rule
        if primary_mapping:
            qs = VendorProductMapping.objects.filter(vendor=vendor, primary_mapping=True)
            if mapping_id:
                qs = qs.exclude(id=mapping_id)
            if qs.exists():
                raise serializers.ValidationError("This vendor already has a primary product mapping.")

        return data

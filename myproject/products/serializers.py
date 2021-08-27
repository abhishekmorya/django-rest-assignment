from rest_framework import fields, serializers

from products import models


class CategorySerializer(serializers.ModelSerializer):
    """Serialiser for Category"""

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'created_on')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create and return created Category"""

        return models.Category.objects.create(**validated_data)


class SubCategorySerializer(serializers.ModelSerializer):
    """Serializer for SubCategory"""

    class Meta:
        model = models.SubCategory
        fields = ('id', 'name',  'category', 'created_on')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create Sub Category and return"""
        return models.SubCategory.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product"""

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'category', 'sub_category', 'created_on')
        read_only_fields = ('id',)

    def validate(self, data):
        print(data)
        exists = models.SubCategory.objects.filter(
            category = data['category'].id,
            id = data['sub_category'].id
        ).exists()
        print('exists', exists)
        if not exists:
            raise serializers.ValidationError('Invalid Category and Sub Category group')
        return data

    def create(self, validated_data):
        """Create Product and return"""

        return models.Product.objects.create(**validated_data)
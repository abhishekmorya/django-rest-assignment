from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response


from products import models
from products import serializers


class CategoryApiView(viewsets.ReadOnlyModelViewSet):
    """API View for Category"""
    
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class SubCategoryApiView(viewsets.ReadOnlyModelViewSet):
    """API View for SubCategory"""

    serializer_class = serializers.SubCategorySerializer
    queryset = models.SubCategory.objects.all()

    def retrieve(self, response, pk):
        category = models.Category.objects.filter(
            name = pk
        ).first()
        queryset = models.SubCategory.objects.filter(category = category.id)
        values = [x.to_dict() for x in queryset]

        return Response(values)


class ProductApiView(viewsets.ModelViewSet):
    """API View for Product"""

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    
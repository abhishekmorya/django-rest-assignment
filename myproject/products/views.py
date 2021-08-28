from rest_framework import viewsets, filters, mixins
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


class ProductApiView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """API View for Product"""

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class ProductSubCategoryView(viewsets.ReadOnlyModelViewSet):
    """Products for a sub-category"""

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    def retrieve(self, request, pk):
        sub_category = models.SubCategory.objects.filter(
            name = pk
        ).first()

        if sub_category is None:
            return Response("Error: Sub Category not found", 404)

        queryset = models.Product.objects.filter(sub_category = sub_category.id)
        values = [x.to_dict() for x in queryset]
        return Response(values)


class ProductCategoryView(viewsets.ReadOnlyModelViewSet):
    """Product for a category"""

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

    def retrieve(self, request, pk):
        category = models.Category.objects.filter(
            name = pk
        ).first()
        if category is None:
            return Response("Error: Category Not Found", 404)
        q = self.queryset.filter(
            category = category.id
        )
        values = [x.to_dict() for x in q]
        return Response(values)
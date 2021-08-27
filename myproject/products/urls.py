from rest_framework.routers import DefaultRouter
from django.urls import include, path

from products import views

router = DefaultRouter()
router.register('category', views.CategoryApiView)
router.register('sub-category', views.SubCategoryApiView)
router.register('product', views.ProductApiView)
# router.register


urlpatterns = [
    path('', include(router.urls)),
]
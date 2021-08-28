from django.db import models


class Category(models.Model):
    """Category Model"""

    name = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def to_dict(self):
        return {
            'id': self.id, 
            'name': self.name, 
            'created_on': self.created_on,
        }

    def __str__(self):
        """Return model as a string"""
        return self.name


class SubCategory(models.Model):
    """SubCategory Model linked to Category"""
    category = models.ForeignKey(
        Category, default='category', on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id, 
            'name': self.name, 
            'category': self.category.name, 
            'created_on': self.created_on,
        }

    def __str__(self):
        """Return the model as a string"""
        return self.name


class Product(models.Model):
    """Products model linked to SubCategory"""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category.name,
            'sub-category': self.sub_category.name,
            'created_on': self.created_on,
        }

    def __str__(self):
        """Return model as string"""
        return self.name

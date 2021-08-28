# django-rest-assignment
Django Rest Framework Assignment

***Endpoints***:
-  "category": "http://localhost:8000/category/",
-  "sub-category": "http://localhost:8000/sub-category/",
-  "product": "http://localhost:8000/product/category/",
-  "product/sub-category": "http://localhost:8000/product/category/",
-  "product/category": "http://localhost:8000/product/category/"

***Details for endpoints for `GET` request:***
1. category: To retrieve all the categories
2. sub-category: To retrieve all the sub categories
3. product: To retrieve all the products
4. product/category: To retrieve all products for a category
5. product/sub-category: To retrieve all products for a sub category

***Details for endpoints for `POST` request:***

product: To add new product for existing category and sub category.

Request Body:

`{
  'name': 'Product Name',
  'category': 'category id',
  'sub-category': 'sub category id'
}`

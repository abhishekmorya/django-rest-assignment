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
***Request Body:***
```
{
  'name': 'Product Name',
  'category': 'category id',
  'sub-category': 'sub category id'
}
```

## Usage for windows
1. Install python3
2. Create virtual environment `myenv` and make it ready to use
   ```
   # Create virtual environment myenv
   python venv -m myenv
   # Activate the environment
   myenv\Scripts\activate.bat
   # Install required python packages by using requirements.txt
   pip install -r requirements.txt
   # Now environment is ready
   ```
3. Clone the repo, move to `django-rest-assignment\myproject` and start development server.
   ```
   cd django-rest-assignment\myproject
   python manage.py runserver
   ```
4. Now all ready to use the rest API.

THANKS...

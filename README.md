# Book API with Django

# Steps to set up your Django Project

1. Create a virtual environment for linux/mac `python3 -m venv venv`. For windows `py -m venv venv`
2. Active the virtual environment for linux/mac `source venv/bin/activate`. For windows cmd `venv\Scripts\activate.bat`
3. Install Django `pip install django`
4. Install Django Rest Framework `pip install djangorestframework`
5. Start project `django-admin startproject books`
6. Create App `python manage.py startapp book_api`
7. Run the server `python manage.py runserver`

# Steps to create tables

1. Create your models in a models.py file
2. Migrate `python manage.py makemigrations`, the table is not created yet.
3. Create the table `python manage.py migrate`

# Steps to upload project to Github

1. Create a requirements.txt file `pip freeze > requirements.txt`
2. Initialize your git repository and commit the data.

# Steps to download from Github

1. Clone the repository
2. Create a vitual environment
3. Execute `pip install -r requirements.txt`

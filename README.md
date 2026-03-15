# django learning management api

my personal project to build a learning management backend using django rest framework.

i built this completely from scratch to get better at DRF. i specifically challenged myself to avoid using generic viewsets or shortcuts, so every single endpoint is written manually using strictly `APIView`. 

## what it does
it basically manages 4 main things:
- vendors
- products
- courses
- certifications

it also handles the mappings between them (like assigning a product to a vendor, or a course to a product). i wrote custom validation in the serializers to make sure you can't add duplicate mappings or mess up the primary mapping rules.

you can also filter the mapping lists using query params like `?vendor_id=1`.

## how to run this locally

1. set up a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # if you are on windows
   ```
2. install the packages:
   ```bash
   pip install django djangorestframework drf-yasg
   ```
3. run the migrations to create the sqlite db:
   ```bash
   python manage.py makemigrations core vendor product course certification vendor_product_mapping product_course_mapping course_certification_mapping
   python manage.py migrate
   ```
4. load up some mock data so the db isn't empty:
   ```bash
   python manage.py seed_data
   ```
5. run the server:
   ```bash
   python manage.py runserver
   ```
   then go to `http://127.0.0.1:8000/` in your browser.

## api docs
i added swagger so you don't even need postman to test the routes. once the server is running, just go to `http://127.0.0.1:8000/swagger/`. 

every master entity and every mapping has full GET, POST, PUT, PATCH, and DELETE methods.

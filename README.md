# Django learning management api

I built this completely from scratch to get better at DRF. This is the assignment given by AI Certs company. The main requirement is to avoid using generic viewsets or shortcuts, so every single endpoint is written manually using strictly `APIView`. 

## what it does
It basically manages 4 main things:
- vendors
- products
- courses
- certifications

It also handles the mappings between them (like assigning a product to a vendor, or a course to a product). I wrote custom validation in the serializers to make sure you can't add duplicate mappings or mess up the primary mapping rules.

You can also filter the mapping lists using query params like `?vendor_id=1`.

## How to run this locally

1. Set up a virtual environment and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # if you are on Windows
   ```
2. Install the packages:
   ```bash
   pip install django djangorestframework drf-yasg
   ```
3. Run the migrations to create the SQLite DB:
   ```bash
   python manage.py makemigrations core vendor product course certification vendor_product_mapping product_course_mapping course_certification_mapping
   python manage.py migrate
   ```
4. Load up some mock data so the DB isn't empty:
   ```bash
   python manage.py seed_data
   ```
5. run the server:
   ```bash
   python manage.py runserver
   ```
   Then go to `http://127.0.0.1:8000/` in your browser.

## Api Docs
I added Swagger, so you don't even need Postman to test the routes. Once the server is running, just go to `http://127.0.0.1:8000/swagger/`. 

Every master entity and every mapping has full GET, POST, PUT, PATCH, and DELETE methods.

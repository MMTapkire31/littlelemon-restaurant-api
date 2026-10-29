LITTLE LEMON RESTAURANT API
Django REST Framework Capstone Project

PROJECT DESCRIPTION
This project combines the Little Lemon booking website with REST API endpoints for menu management, table bookings, user registration, and token authentication. It uses Django, Django REST Framework, and MySQL.

INSTALLATION
1. Create a MySQL database:
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

2. Copy .env.example to .env and configure MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, and DJANGO_SECRET_KEY. Never commit real credentials.

3. From the folder containing manage.py, install dependencies:
   pip install pipenv
   pipenv install
   pipenv shell
   Alternatively, use a virtual environment and run: pip install -r requirements.txt

4. Apply migrations:
   python manage.py makemigrations restaurant
   python manage.py migrate

5. Run checks and tests:
   python manage.py check
   python manage.py test

6. Start server:
   python manage.py runserver

WEBSITE PAGES
Home: http://127.0.0.1:8000/
Booking form: http://127.0.0.1:8000/book/
Reservations: http://127.0.0.1:8000/reservations/
All reservation JSON: http://127.0.0.1:8000/bookings/
Date-filtered reservations: http://127.0.0.1:8000/bookings/?date=YYYY-MM-DD

API ENDPOINTS
Menu:
GET /restaurant/menu/       List menu items (public)
GET /restaurant/menu/1/     Retrieve a menu item (public)
POST /restaurant/menu/      Create a menu item (authentication required)
PUT/PATCH /restaurant/menu/1/ Update a menu item (authentication required)
DELETE /restaurant/menu/1/ Delete a menu item (authentication required)

Bookings:
GET /restaurant/booking/       List bookings (public)
GET /restaurant/booking/1/     Retrieve a booking (public)
POST /restaurant/booking/      Create a booking (authentication required)
PUT/PATCH /restaurant/booking/1/ Update a booking (authentication required)
DELETE /restaurant/booking/1/ Delete a booking (authentication required)

Registration and token authentication:
POST /restaurant/registration/
JSON: {"username":"demo","email":"demo@example.com","password":"UseAUniquePassword123!"}
POST /restaurant/api-token-auth/
JSON: {"username":"demo","password":"UseAUniquePassword123!"}
For protected requests, set header: Authorization: Token YOUR_TOKEN_VALUE

INSOMNIA TESTING
Use the methods and URLs above. For POST/PUT/PATCH, select JSON body.
Menu example: {"title":"Greek salad","price":"12.50","inventory":10}
Booking example: {"first_name":"Alex","reservation_date":"2030-01-02","reservation_slot":"19:00"}
Register, request a token, then add the Authorization header for write operations. Use real IDs from GET responses.

TESTING
Run: python manage.py test
Tests cover public menu listing, permission enforcement, authenticated menu creation, booking operations, registration, and token login.

DATABASE
MySQL is configured through .env. Booking has a unique constraint on reservation_date + reservation_slot. MenuItem stores title, price, and inventory.

GITHUB
Replace with your actual repository URL. Never claim a repository exists until you have pushed the code.

SECURITY
Do not commit .env, passwords, tokens, or production secret keys. Current permissions allow any authenticated user to write menu items and bookings; production deployments should use manager and booking-owner permissions.

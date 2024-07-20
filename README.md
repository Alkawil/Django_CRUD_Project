# Django_CRUD_Project
# Django Booking Project

This is a Django project for managing bookings. Users can create, read, update, and delete (CRUD) bookings. Each booking is associated with a category, which is selected from predefined categories.

## Features

- Create, read, update, and delete bookings.
- Categories for bookings, selectable from a dropdown menu.
- Integration with Django's admin interface for managing bookings and categories.

## Models

### Category

The `Category` model represents different categories for bookings.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

### Booking

The Booking model represents a booking with the following fields:

    first_name: First name of the person booking.
    last_name: Last name of the person booking.
    guest_count: Number of guests.
    reservation_time: Date and time of the reservation.
    comments: Additional comments.
    category: Category of the booking (ForeignKey to Category).

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField()
    comments = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

Setup Instructions
### Prerequisites

    Python 3.x
    Django 3.x or higher
    Virtual environment (optional but recommended)

### Installation

    Clone the repository:


git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

### Create and activate a virtual environment (optional but recommended):


python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

### Install the dependencies:

pip install -r requirements.txt

### Create the database and apply migrations:


python manage.py migrate

### Run the development server:

    python manage.py runserver
    
### Create a superuser:


python manage.py createsuperuser

### Usage

    Admin Interface:
        Go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
        You can manage bookings and categories from the admin interface.

    Create Bookings:
        Go to http://127.0.0.1:8000/booking/new/ to create a new booking.
        Fill in the form and submit to save the booking to the database.



### You can create some example categories and bookings using the Django shell:


from myapp.models import Category, Booking
from django.utils import timezone

category1 = Category.objects.create(name='Business')
category2 = Category.objects.create(name='Family')

Booking.objects.create(
    first_name='John',
    last_name='Doe',
    guest_count=2,
    reservation_time=timezone.now(),
    comments='Table by the window',
    category=category1
)

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.
### License

This project is licensed under the MIT License.
Acknowledgements

    Django Documentation: https://docs.djangoproject.com/

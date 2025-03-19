# SolEctro - Electronics Store

## Screenshot

![SolEctro Screenshot](home/static/home/images/sc.png)

## Description
SolEctro is a modern e-commerce platform for electronics, built with Django and Bootstrap. 

## Features
- Responsive product catalog
- Shopping cart with real-time updates
- Product quantity management
- Dynamic cart badge counter
- Price calculations with tax and shipping
- Image upload support
- Stock level tracking
- Admin product management

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/solEctro.git
   cd solEctro
   ```
2. Create and activate virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure the database in settings.py

5. Run migrations:
   ```sh
   python manage.py migrate
   ```

6. Create superuser:
   ```sh
   python manage.py createsuperuser
   ```

7. Run development server:
   ```sh
   python manage.py runserver
   ```

## Usage
1. Visit `/admin` to manage products
2. Browse products on homepage
3. Add products to cart
4. Manage quantities in cart
5. Proceed to checkout

## Technologies
- Django 5.1.7
- PostgreSQL
- Bootstrap 5
- Python 3

## Contributing

Please read CONTRIBUTING.md for details on submitting pull requests.

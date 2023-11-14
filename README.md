![Smar'ket](/readme_images/smartket_desktop.png)
# Smar'ket - a Website for Managing Sari-Sari Store

Smar'ket is a Django website that is used to manage sari-sari stores. The name is derived from the combination of "smart" and "market". The goal of this application is to keep track of all the product information and transactions that happens in the sari-sari store.

## Run Locally

To use this application you have to clone this repository using git bash.

### Clone the repository
- Open the directory you want this application to be cloned. 
- Open git bash.

```bash
git clone https://github.com/AristonCatipay/django_smartket.git
```

### Install Dependencies

Activate virtual environment
```bash
pipenv shell
```

Install Django
```bash
pipenv install django
```

Install MySQL Client
```bash
pipenv install mysqlclient
```

Install Tailwind
```bash
pipenv install django-tailwind
```

Install Django Tailwind Reload
```bash
pipenv install django-tailwind[reload]
```

Create a database named 'django_smartket' 
using your RDMS of choice (in this case using XAMPP Server).

![Create_a_database](/readme_images/xampp_create_database.png)

Edit your database configuration in the settings.py.
![Database_Configuration](/readme_images/change_database_settings.png)

Migrate
```bash
python manage.py migrate
```

Start the server
```bash
python manage.py runserver
```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
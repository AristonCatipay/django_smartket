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

Install Pipenv

```bash
pip install pipenv
```

Activate Virtual Environment

```bash
pipenv shell
```

Make sure you have `Python 3.11`
Go to [Python 11](https://www.python.org/downloads/release/python-3119/)
If you have multiple installation of python. Choose the python 11.

```bash
pipenv --python path\to\python.exe
```

Install Dependencies using the requirements.txt file.

```bash
pip install -r requirements.txt
```

Migrate

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

### Update dependencies

```bash
pipenv update
```

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

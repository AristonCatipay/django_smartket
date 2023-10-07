from django.db import models

class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = '0'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others')
    ]
    
    SINGLE = 'S'
    MARRIED = 'M'
    WIDOW = 'W'

    CIVIL_STATUS_CHOICES = [
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (WIDOW, 'Widow')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)
    email = models.EmailField(max_length=100, unique=True)
    contact_no = models.CharField(max_length=15, unique=True)
    civil_status = models.CharField(max_length=1, choices=CIVIL_STATUS_CHOICES, default=SINGLE)
    street = models.CharField(max_length=255)
    barangay = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

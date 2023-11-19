from django.contrib.auth.models import User
from django.db import models
 
class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'O'),
    ]

    image = models.ImageField(upload_to='profile_images', default='default_profile_image.jpg')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=OTHERS)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

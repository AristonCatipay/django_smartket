from django.db import models
from customer.models import Customer

class Number(models.Model):
    GLOBE = 'GLOBE'
    SMART = 'SMART'
    TNT = 'TNT'
    SUN = 'SUN'
    TM = 'TM'
    DITO = 'DITO'
    GOMO = 'GOMO'
    DEFAULT = 'Not Specified'

    NETWORK_CHOICES = [
        (GLOBE, 'Globe'),
        (SMART, 'Smart'),
        (TNT, 'TNT'), 
        (SUN, 'Sun'),
        (TM, 'TM'),
        (DITO, 'Dito'),
        (GOMO, 'Gomo'),
        (DEFAULT, 'Not Specified')
    ]

    customer = models.ForeignKey(Customer, related_name='customer_id',on_delete=models.CASCADE)
    number = models.CharField(max_length=150, unique=True)
    network = models.CharField(max_length=25, choices=NETWORK_CHOICES, default=DEFAULT)
    load = models.CharField(max_length=150)
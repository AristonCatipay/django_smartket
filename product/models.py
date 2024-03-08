from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Metric_Unit(models.Model):
    name = models.CharField(max_length=255)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name
    
# Predefined metric units
PREDEFINED_UNITS = [
    "Grams",
    "Kilograms",
    "Milliliters",
    "Liters",
    "Pieces",
    "Pair",
    "Pack",
    "Dozens",
    "Not Specified"
]

@receiver(post_migrate)
def check_metric_units(sender, **kwargs):
    # Check if Metric_Unit table is empty
    if Metric_Unit.objects.count() == 0:
        # If empty, populate with predefined metric units
        for unit_name in PREDEFINED_UNITS:
            Metric_Unit.objects.create(name=unit_name)
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Setting the right plural name in the admin site.
        verbose_name_plural = 'Categories'
        # Setting the name field in alphabetical order.
        ordering = ('name',)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name

PREDEFINED_CATEGORIES = [
    "Can Goods",
    "Sauces",
    "Drinks and Beverages",
    "Coffee and Sugar",
    "Frozen Food",
    "Milk and Dairy",
    "Noodles",
    "Cup Noodles",
    "Soup and Shampoo",
    "Chemicals",
    "Medicine",
    "Crackers",
    "Diaper",
    "Not Specified"
]

@receiver(post_migrate)
def check_categories(sender, **kwargs):
    # Check if Category table is empty
    if Category.objects.count() == 0:
        # If empty, populate with predefined categories
        for category_name in PREDEFINED_CATEGORIES:
            Category.objects.create(name=category_name)

class Color(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Setting the name field in alphabetical order.
        ordering = ('name',)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name
    
PREDEFINED_COLORS = [
    "Red",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Violet",
    "Pink",
    "White",
    "Grey",
    "Black",
    "Not Specified"
]

@receiver(post_migrate)
def check_colors(sender, **kwargs):
    # Check if Color table is empty
    if Color.objects.count() == 0:
        # If empty, populate with predefined colors
        for color_name in PREDEFINED_COLORS:
            Color.objects.create(name=color_name)

class Size(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Setting the name field in alphabetical order.
        ordering = ('name',)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name

# Predefined sizes
PREDEFINED_SIZES = [
    "Extra Small",
    "Small",
    "Medium",
    "Large",
    "Extra Large",
    "Double XL",
    "Triple XL",
    "Not Specified"
]

@receiver(post_migrate)
def check_sizes(sender, **kwargs):
    # Check if Size table is empty
    if Size.objects.count() == 0:
        # If empty, populate with predefined sizes
        for size_name in PREDEFINED_SIZES:
            Size.objects.create(name=size_name)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    metric_number = models.CharField(max_length=255)
    metric_unit = models.ForeignKey(Metric_Unit, related_name='metric_id', on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE)
    product_color = models.ForeignKey(Color, related_name='color_id', on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, related_name='size_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name



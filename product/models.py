from django.db import models

class Metric_Unit(models.Model):
    name = models.CharField(max_length=255)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name
    
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
    
    # Different Categories
    # Can goods
    # Sauces
    # Drinks and Beverages
    # Coffee and Sugar
    # Frozen Food
    # Milk and Dairy
    # Noodles
    # Cup Noodles
    # Soup and Shampoo
    # Chemicals
    # Medicine
    # Crackers
    # Diaper
    # Not Specified

class Color(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Setting the name field in alphabetical order.
        ordering = ('name',)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name
    
    # Different Color
    # Red
    # Orange
    # Yellow
    # Green
    # Blue
    # Violet
    # Pink
    # White
    # Grey
    # Black
    # Not Specified

class Size(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        # Setting the name field in alphabetical order.
        ordering = ('name',)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name
    
    # Different Sizes
    # Extra Small
    # Small
    # Medium
    # Large
    # Extra Large
    # Double XL
    # Triple XL
    # Not Specified


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    metric_number = models.CharField(max_length=255)
    metric_unit = models.ForeignKey(Metric_Unit, related_name='metric_id', on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, related_name='category_id', on_delete=models.CASCADE)
    product_color = models.ForeignKey(Color, related_name='color_id', on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, related_name='size_id', on_delete=models.CASCADE)




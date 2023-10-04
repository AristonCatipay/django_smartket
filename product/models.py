from django.db import models

class Metric_Unit(models.Model):
    name = models.CharField(max_length=255)

    # Showing the actual name of the field.
    def __str__(self):
        return self.name

class Product(models.Model):
    RED = 'R'
    ORANGE = 'O'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    VIOLET = 'V'
    PINK = 'P'
    WHITE = 'W'
    GREY = 'GY'
    BLACK = 'BK'
    COLOR_NOT_SPECIFIED = 'NS'

    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (VIOLET, 'Violet'),
        (PINK, 'Pink'),
        (WHITE, 'White'),
        (GREY, 'Grey'),
        (BLACK, 'Black'),
        (COLOR_NOT_SPECIFIED, 'Not Specified'),
    ]

    CAN_GOODS = 'CG'
    SAUCES = 'S'
    DRINKS_BEVERAGES = 'DB'
    COFFEE_SUGAR = 'CS'
    FROZEN_FOOD = 'FF'
    MILK_DAIRY = 'MD'
    NOODLES = 'N'
    CUP_NOODLES = 'CN'
    SOUP_SHAMPOO = 'SS'
    CHEMICALS = 'C'
    MEDICINE = 'M'
    CRACKERS = 'CK'
    DIAPER = 'D'
    SECTION_NOT_SPECIFIED = 'NS'

    SECTION_CHOICES = [
        (CAN_GOODS, 'Can Goods'),
        (SAUCES, 'Sauces'),
        (DRINKS_BEVERAGES, 'Drinks and Beverages'),
        (COFFEE_SUGAR, 'Coffee and Sugar'),
        (FROZEN_FOOD, 'Frozen Food'),
        (MILK_DAIRY, 'Milk and Dairy'),
        (NOODLES, 'Noodles'),
        (CUP_NOODLES, 'Cup Noodles'),
        (SOUP_SHAMPOO, 'Soup and Shampoo'),
        (CHEMICALS, 'Chemicals'),
        (MEDICINE, 'Medicine'),
        (CRACKERS, 'Crackers'),
        (DIAPER, 'Diaper'),
        (SECTION_NOT_SPECIFIED, 'Not Specified'),
    ]

    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    DOUBLE_XL = 'XXL'
    TRIPLE_XL = 'XXXL'
    SIZE_NOT_SPECIFIED = 'NS'

    SIZE_CHOICES = [
        (EXTRA_SMALL, 'Extra Small'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (EXTRA_LARGE, 'Extra Large'),
        (DOUBLE_XL, 'Double XL'),
        (TRIPLE_XL, 'Triple XL'),
        (SIZE_NOT_SPECIFIED, 'Not Specified'),
    ]


    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()
    metric_number = models.CharField(max_length=255)
    metric_unit = models.ForeignKey(Metric_Unit, related_name='metric_id', on_delete=models.CASCADE)
    product_color = models.CharField(max_length=2, choices=COLOR_CHOICES, default=COLOR_NOT_SPECIFIED)
    product_section = models.CharField(max_length=2, choices=SECTION_CHOICES, default=SECTION_NOT_SPECIFIED)
    product_size = models.CharField(max_length=4, choices=SIZE_CHOICES, default=SIZE_NOT_SPECIFIED)




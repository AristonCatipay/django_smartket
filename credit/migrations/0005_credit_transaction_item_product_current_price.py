# Generated by Django 4.2.7 on 2023-11-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0004_credit_transaction_credit_transaction_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit_transaction_item',
            name='product_current_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-13 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_quote_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='total_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
# Generated by Django 3.2 on 2022-04-08 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0003_category_cat_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat_image',
        ),
    ]
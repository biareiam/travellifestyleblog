# Generated by Django 3.2 on 2022-02-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0014_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, default='placeholder', null=True, upload_to='images/'),
        ),
    ]

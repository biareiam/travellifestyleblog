# Generated by Django 3.2 on 2022-02-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0019_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

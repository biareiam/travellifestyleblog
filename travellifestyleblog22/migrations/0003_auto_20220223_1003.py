# Generated by Django 3.2 on 2022-02-23 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0002_post_title_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='post_title',
        ),
    ]

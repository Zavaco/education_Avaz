# Generated by Django 3.1.2 on 2020-11-15 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0049_category_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_slug',
            new_name='slug',
        ),
    ]

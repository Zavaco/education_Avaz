# Generated by Django 3.1.2 on 2020-11-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20201106_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_featuredcourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuredcourses',
            name='fc_price',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20201113_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_remove_course_course_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.1.2 on 2020-11-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_teacher_teacher_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

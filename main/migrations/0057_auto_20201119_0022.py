# Generated by Django 3.1.2 on 2020-11-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_auto_20201118_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_name',
            field=models.CharField(default='John Smith', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(default='Password', max_length=50),
        ),
    ]

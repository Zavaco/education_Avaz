# Generated by Django 3.1.2 on 2020-11-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_userrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrequest',
            name='user_status',
            field=models.BooleanField(null=True, verbose_name='checked'),
        ),
    ]

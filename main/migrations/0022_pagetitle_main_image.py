# Generated by Django 3.1.2 on 2020-11-05 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20201105_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetitle',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

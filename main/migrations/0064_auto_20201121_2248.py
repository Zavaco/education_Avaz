# Generated by Django 3.1.2 on 2020-11-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_auto_20201121_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

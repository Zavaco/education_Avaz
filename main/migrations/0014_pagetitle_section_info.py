# Generated by Django 3.1.2 on 2020-11-03 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_pagetitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetitle',
            name='section_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.menu'),
        ),
    ]
# Generated by Django 3.1.2 on 2020-11-03 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_pagetitle_section_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagetitle',
            name='section_info',
        ),
        migrations.AddField(
            model_name='menu',
            name='section_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.pagetitle'),
        ),
    ]
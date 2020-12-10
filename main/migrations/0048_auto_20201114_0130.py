# Generated by Django 3.1.2 on 2020-11-13 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_auto_20201114_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

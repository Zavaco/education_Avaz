# Generated by Django 3.1.2 on 2020-11-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_auto_20201121_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-03 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_footerinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footerinfo',
            old_name='footer_title',
            new_name='title_development',
        ),
        migrations.AddField(
            model_name='footerinfo',
            name='title_engineering',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='footerinfo',
            name='title_graphics',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
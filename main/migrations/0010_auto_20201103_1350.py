# Generated by Django 3.1.2 on 2020-11-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_footerinfo_footer_to'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FooterInfo',
        ),
        migrations.AddField(
            model_name='menu',
            name='title_development',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_engineering',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_graphics',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
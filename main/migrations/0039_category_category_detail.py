# Generated by Django 3.1.2 on 2020-11-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_footerinfo_footer_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]

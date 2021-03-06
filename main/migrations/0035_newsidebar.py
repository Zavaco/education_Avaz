# Generated by Django 3.1.2 on 2020-11-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_pagenew'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ns_categories', models.CharField(blank=True, max_length=50, null=True)),
                ('ns_month', models.CharField(blank=True, max_length=50, null=True)),
                ('ns_archives', models.CharField(blank=True, max_length=50, null=True)),
                ('ns_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]

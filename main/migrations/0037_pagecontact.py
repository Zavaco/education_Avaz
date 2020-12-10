# Generated by Django 3.1.2 on 2020-11-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20201107_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_contact_bg', models.ImageField(blank=True, null=True, upload_to='')),
                ('p_form_title', models.CharField(max_length=50, null=True)),
                ('p_form_info', models.CharField(max_length=250, null=True)),
                ('p_sidebar_title', models.CharField(max_length=50, null=True)),
                ('p_sidebar_info', models.CharField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
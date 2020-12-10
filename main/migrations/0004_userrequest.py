# Generated by Django 3.1.2 on 2020-11-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201102_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('user_phone', models.CharField(max_length=50, null=True)),
                ('user_status', models.BooleanField(verbose_name='checked')),
                ('request_message', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'User_Request',
                'verbose_name_plural': 'User_Requests',
            },
        ),
    ]
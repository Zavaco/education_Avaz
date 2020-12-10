# Generated by Django 3.1.2 on 2020-11-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_title', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='title_development',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='title_engineering',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='title_graphics',
        ),
    ]

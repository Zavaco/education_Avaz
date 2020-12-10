# Generated by Django 3.1.2 on 2020-11-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201103_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_engineering', models.CharField(max_length=50, null=True)),
                ('title_graphics', models.CharField(max_length=50, null=True)),
                ('title_development', models.CharField(max_length=50, null=True)),
                ('footer_order', models.IntegerField(verbose_name='order')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Footer_Info',
                'verbose_name_plural': 'Footer_Informs',
            },
        ),
    ]
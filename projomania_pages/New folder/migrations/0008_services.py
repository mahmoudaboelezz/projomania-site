# Generated by Django 3.2.7 on 2021-10-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projomania_pages', '0007_auto_20211010_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainService', models.CharField(max_length=100, verbose_name='Main')),
            ],
        ),
    ]
# Generated by Django 3.2.7 on 2021-12-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projomania_pages', '0029_auto_20211213_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-13 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projomania_pages', '0022_auto_20211114_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time added'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updates',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Updated'),
        ),
        migrations.AlterField(
            model_name='ticket_reply',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time added'),
        ),
    ]

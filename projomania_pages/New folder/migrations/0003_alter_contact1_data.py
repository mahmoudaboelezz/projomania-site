# Generated by Django 3.2.7 on 2021-09-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projomania_pages', '0002_auto_20210930_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact1',
            name='data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
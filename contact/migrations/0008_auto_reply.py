# Generated by Django 3.2.7 on 2021-12-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20211202_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto_Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.TextField()),
                ('solution', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]

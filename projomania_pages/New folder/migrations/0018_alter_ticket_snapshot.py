# Generated by Django 3.2.7 on 2021-11-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projomania_pages', '0017_alter_ticket_snapshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='snapShot',
            field=models.ImageField(default='default.png', upload_to='photos1/%y/%m/%d'),
        ),
    ]

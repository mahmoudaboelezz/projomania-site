# Generated by Django 3.2.7 on 2021-12-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_auto_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='comment',
        ),
        migrations.AddField(
            model_name='ticket',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='solution',
            field=models.TextField(blank=True, null=True),
        ),
    ]
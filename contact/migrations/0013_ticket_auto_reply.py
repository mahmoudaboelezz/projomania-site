# Generated by Django 3.2.7 on 2021-12-28 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211228_2155'),
        ('contact', '0012_delete_auto_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='auto_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.auto_reply'),
        ),
    ]
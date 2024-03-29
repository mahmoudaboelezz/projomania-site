# Generated by Django 3.2.7 on 2021-10-19 18:29

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projomania_pages', '0011_auto_20211018_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='SpecialOrder',
            field=models.CharField(blank=True, default='None', max_length=100, null=True, verbose_name='Special'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='my_field',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ODOO DEVELOPMENT', 'ODOO DEVELOPMENT'), ('CODE UPGRADING', 'CODE UPGRADING'), ('DATABASE MIGRATION', 'DATABASE MIGRATION'), ('LINUX ADMINISTRATION', 'LINUX ADMINISTRATION')], default='none', max_length=71),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companies',
            name='companyLogo',
            field=models.ImageField(default="{% static 'default.png' %}", upload_to='photos/%y/%m/%d'),
        ),
    ]

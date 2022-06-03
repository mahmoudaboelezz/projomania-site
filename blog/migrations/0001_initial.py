# Generated by Django 3.2.7 on 2021-12-14 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(default='default.png', upload_to='', verbose_name='thumbnails')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, verbose_name='URL IN SITE')),
                ('title', models.CharField(max_length=30)),
                ('blog', models.TextField()),
                ('category', models.CharField(blank=True, choices=[('Database Migration', 'Database Migration'), ('Odoo Development', 'Odoo Development')], default='none', max_length=50, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

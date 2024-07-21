# Generated by Django 5.0.6 on 2024-07-16 14:14

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=150)),
                ('pro_bio', models.CharField(max_length=150)),
                ('pro_dob', models.DateField(blank=True, default=datetime.datetime.now)),
                ('pro_pic', models.ImageField(upload_to='pro_image/')),
                ('pro_number', models.CharField(max_length=10, null=True)),
                ('pro_cv', models.FileField(upload_to='pdfs/')),
                ('pro_certificates', models.FileField(upload_to='pdfs/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

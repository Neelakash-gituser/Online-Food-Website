# Generated by Django 3.0.8 on 2020-09-14 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0006_purchase'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
# Generated by Django 3.0.8 on 2020-09-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0003_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(default='', upload_to='static/Food'),
        ),
    ]
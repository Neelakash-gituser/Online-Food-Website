# Generated by Django 3.0.8 on 2020-09-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('food_desc', models.CharField(max_length=300)),
            ],
        ),
    ]
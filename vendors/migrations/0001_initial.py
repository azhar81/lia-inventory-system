# Generated by Django 4.1.1 on 2022-11-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
    ]

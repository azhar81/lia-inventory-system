# Generated by Django 4.1.1 on 2022-11-13 12:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendors', '__first__'),
        ('locations', '__first__'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'Normal'), (2, 'Perlu diperiksa'), (3, 'Diperbaiki'), (4, 'Dipinjam'), (5, 'Rusak')], default=1)),
                ('merk', models.CharField(blank=True, max_length=100)),
                ('price', models.FloatField()),
                ('datePurchased', models.DateField(default=datetime.date.today)),
                ('warrantyYears', models.IntegerField()),
                ('usefulLife', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='locations.location')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='vendors.vendor')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='DynamicAsset',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('assets.asset',),
        ),
        migrations.CreateModel(
            name='StaticAsset',
            fields=[
                ('asset_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assets.asset')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('assets.asset',),
        ),
    ]

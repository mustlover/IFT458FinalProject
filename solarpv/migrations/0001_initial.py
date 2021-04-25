# Generated by Django 3.1.7 on 2021-03-28 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='', max_length=100)),
                ('client_type', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.CharField(default='', max_length=100)),
                ('product_name', models.CharField(default='', max_length=100)),
                ('length', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('cell_technology', models.CharField(default='', max_length=100)),
                ('cell_manufacturer', models.CharField(default='', max_length=100)),
                ('number_of_cells', models.IntegerField(default=0)),
                ('number_of_cells_in_series', models.IntegerField(default=0)),
                ('number_of_series_strings', models.IntegerField(default=0)),
                ('number_of_bypass_diodes', models.IntegerField(default=0)),
                ('superstrate_type', models.CharField(default='', max_length=100)),
                ('superstrate_manufacturer', models.CharField(default='', max_length=100)),
                ('substrate_type', models.CharField(default='', max_length=100)),
                ('substrate_manufacturer', models.CharField(default='', max_length=100)),
                ('frame_type', models.CharField(default='', max_length=100)),
                ('frame_adhesive', models.CharField(default='', max_length=100)),
                ('encapsulant_type', models.CharField(default='', max_length=100)),
                ('encapsulant_manufacturer', models.CharField(default='', max_length=100)),
                ('junction_box_type', models.CharField(default='', max_length=100)),
                ('junction_box_manufacturer', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('is_fi_required', models.BooleanField(default=False)),
                ('fi_frequency', models.CharField(default='', max_length=100)),
                ('standard_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solarpv.teststandard')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_system_voltage', models.IntegerField(default=0)),
                ('voc', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('isc', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('vmp', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('imp', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pmp', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ff', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('model_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solarpv.product')),
                ('sequence_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solarpv.testsequence')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(default='', max_length=100)),
                ('address2', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('postal_code', models.CharField(default='', max_length=10)),
                ('country', django_countries.fields.CountryField(default='', max_length=2)),
                ('phone_number', models.CharField(default='', max_length=100)),
                ('fax_number', models.CharField(default='', max_length=100)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='solarpv.client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(default='', max_length=100)),
                ('report_number', models.CharField(default='', max_length=100)),
                ('issue_date', models.DateField()),
                ('location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solarpv.location')),
                ('model_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solarpv.product')),
                ('standard_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='solarpv.teststandard')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

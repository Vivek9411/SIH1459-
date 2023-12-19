# Generated by Django 5.0 on 2023-12-18 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_scheme_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Branch Name')),
                ('code', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(99)], verbose_name='Scheme Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Course Creation Date')),
            ],
        ),
        migrations.AlterField(
            model_name='college',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(99999)], verbose_name='State Code'),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='State Code'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='Course Duration'),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(999)], verbose_name='Scheme Id'),
        ),
        migrations.AlterField(
            model_name='state',
            name='code',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(99)], verbose_name='State Code'),
        ),
        migrations.AlterField(
            model_name='student',
            name='aadhar_id',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100000000000), django.core.validators.MaxValueValidator(999999999999)], verbose_name='Aadhar id'),
        ),
        migrations.AlterField(
            model_name='student',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(1000000000000), django.core.validators.MaxValueValidator(9999999999999)], verbose_name='UID'),
        ),
    ]
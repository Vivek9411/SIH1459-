# Generated by Django 5.0 on 2023-12-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_course_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='id',
            field=models.DecimalField(decimal_places=0, max_digits=2, max_length=2, primary_key=True, serialize=False, verbose_name='Scheme Id'),
        ),
    ]

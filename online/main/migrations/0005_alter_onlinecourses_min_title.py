# Generated by Django 4.0.4 on 2022-06-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_onlinecourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinecourses',
            name='min_title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='logo',
            field=models.ImageField(default='', upload_to='upload'),
        ),
    ]
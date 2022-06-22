# Generated by Django 4.0.4 on 2022-06-11 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=300)),
                ('author_text', models.TextField()),
                ('data', models.DateField()),
                ('post_name', models.CharField(max_length=300)),
                ('logo1', models.ImageField(upload_to='upload')),
                ('logo2', models.ImageField(upload_to='upload')),
                ('info1', models.TextField()),
                ('info2', models.TextField()),
                ('info3', models.TextField()),
                ('info4', models.TextField()),
                ('plus_post_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('count_courses', models.IntegerField(default=0)),
                ('popular', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.IntegerField()),
                ('twitter', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('linkedIn', models.CharField(max_length=300)),
                ('instagram', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('text', models.TextField()),
                ('profession', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('profession', models.CharField(max_length=300)),
                ('level', models.IntegerField(default=0)),
                ('is_main', models.BooleanField()),
                ('twitter', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('linkedIn', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('count_students', models.IntegerField(default=0)),
                ('duration', models.TimeField()),
                ('rating', models.IntegerField(default=0)),
                ('reviews', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('comments_count', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=300)),
                ('short_title', models.CharField(max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('text', models.TextField()),
                ('data', models.DateField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.blog')),
            ],
        ),
    ]

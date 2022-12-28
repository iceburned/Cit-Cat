# Generated by Django 4.1.3 on 2022-12-14 09:50

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True,
                                           validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('date_created', models.TimeField(auto_now=True)),
                ('logo', models.ImageField(default='', upload_to='forum/static_images')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForumSubcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True,
                                           validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('date_created', models.TimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForumTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)])),
                ('content', models.TextField(blank=True, max_length=255, null=True)),
                ('date_created', models.TimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('subcategory',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forumsubcategories')),
            ],
        ),
    ]

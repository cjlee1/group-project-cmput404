# Generated by Django 2.1.5 on 2019-03-29 05:52

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', models.TextField(default='')),
                ('is_markdown', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ignored', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(default='')),
                ('body', models.TextField()),
                ('image_link', models.FileField(blank=True, null=True, upload_to='')),
                ('privacy_setting', models.CharField(choices=[('1', 'me'), ('2', 'specific users'), ('3', 'my friends'), ('4', 'friends of friends'), ('5', 'only friends on my host'), ('6', 'public')], default='1', max_length=1)),
                ('is_markdown', models.BooleanField(default=False)),
                ('is_unlisted', models.BooleanField(default=False)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('original_host', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PostAuthorizedAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(max_length=250)),
                ('post_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_cat_id', to='API.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host', models.URLField(default='', unique=True)),
                ('username', models.TextField(default='', max_length=255, unique=True)),
                ('password', models.CharField(default='', max_length=255)),
            ],
        ),
    ]

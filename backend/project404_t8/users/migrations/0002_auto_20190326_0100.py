# Generated by Django 2.1.5 on 2019-03-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='displayname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
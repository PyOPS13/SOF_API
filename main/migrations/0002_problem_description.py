# Generated by Django 3.1 on 2021-08-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
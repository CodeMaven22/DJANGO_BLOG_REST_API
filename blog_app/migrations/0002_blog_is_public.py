# Generated by Django 5.0.4 on 2024-05-03 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]

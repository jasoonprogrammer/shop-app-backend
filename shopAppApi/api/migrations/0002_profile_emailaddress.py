# Generated by Django 5.0.6 on 2024-05-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emailAddress',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.7 on 2024-09-03 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniprojects',
            name='live_url',
            field=models.URLField(blank=True),
        ),
    ]

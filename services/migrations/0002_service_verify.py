# Generated by Django 2.1.4 on 2018-12-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='verify',
            field=models.BooleanField(default=True),
        ),
    ]
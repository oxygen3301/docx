# Generated by Django 3.1.4 on 2020-12-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='pulse',
            field=models.IntegerField(null=True),
        ),
    ]
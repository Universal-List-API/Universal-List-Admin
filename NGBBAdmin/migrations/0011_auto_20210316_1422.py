# Generated by Django 3.1.7 on 2021-03-16 14:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('NGBBAdmin', '0010_auto_20210316_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalbotlistfeature',
            name='id',
        ),
        migrations.AlterField(
            model_name='historicalbotlist',
            name='api_token',
            field=models.TextField(default=uuid.UUID('9b60df8b-f64b-4cde-b51e-9c13d18b5b09')),
        ),
    ]
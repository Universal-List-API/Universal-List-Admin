# Generated by Django 3.1.7 on 2021-03-16 12:25

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('NGBBAdmin', '0005_auto_20210316_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalbotlist',
            name='api_token',
            field=models.TextField(default=uuid.UUID('cdfd1e34-5b44-4aa6-b2aa-84ffe0952a2d')),
        ),
        migrations.AlterField(
            model_name='historicalbotlist',
            name='owners',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), default=[], size=None),
        ),
    ]

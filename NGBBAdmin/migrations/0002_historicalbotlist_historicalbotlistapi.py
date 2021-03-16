# Generated by Django 3.1.7 on 2021-03-16 12:22

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NGBBAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBotListApi',
            fields=[
                ('method', models.IntegerField(choices=[(1, 'GET'), (2, 'POST'), (3, 'PATCH'), (4, 'PUT'), (5, 'DELETE')], null=True)),
                ('feature', models.IntegerField(choices=[(1, 'Get Bot'), (2, 'Post Stats')], default=1, null=True)),
                ('supported_fields', models.JSONField(help_text='Format of each key, valae is NGBB_KEY: LIST_KEY where NGBB_KEY is the key used by NGBB and LIST_KEY is the key used by the list')),
                ('api_path', models.TextField(default='', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('url', models.ForeignKey(blank=True, db_column='url', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='NGBBAdmin.botlist')),
            ],
            options={
                'verbose_name': 'historical bot list api',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalBotList',
            fields=[
                ('icon', models.TextField(blank=True, null=True)),
                ('url', models.TextField(db_index=True)),
                ('api_url', models.TextField(blank=True, null=True)),
                ('discord', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('supported_features', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None)),
                ('api_token', models.TextField(default=uuid.UUID('bbdfafc7-9fc3-4a90-acc9-1e8ecd24e7dd'))),
                ('queue', models.BooleanField(default=False, null=True)),
                ('owners', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), blank=True, null=True, size=None)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical bot list',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
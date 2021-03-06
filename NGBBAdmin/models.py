from django.db import models
from django.contrib.postgres.fields import ArrayField
from simple_history import register
import uuid
from .config import *

# Create your models here.

class BotList(models.Model):
    icon = models.TextField(blank=True, null=True)
    url = models.TextField(unique=True, primary_key = True)
    api_url = models.TextField(blank=True, null=True)
    discord = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supported_features = ArrayField(base_field = models.IntegerField(), blank=True, null=True)
    api_token = models.TextField(blank=False, null=False, default = uuid.uuid4())
    queue = models.BooleanField(blank=False, null=False, default=False)
    owners = ArrayField(base_field = models.BigIntegerField(), blank=False, null=False, default=list)

    class Meta:
        managed = False
        db_table = 'bot_list'

    def __str__(self):
        return self.url

register(BotList)

class BotListApi(models.Model):
    id = models.AutoField(primary_key = True)
    url = models.ForeignKey(BotList, on_delete = models.CASCADE, db_column = 'url', db_constraint = False, unique = False, db_index = False, blank = True)
    method = models.IntegerField(blank=False, null=False, choices = method_choices, default=1)
    feature = models.IntegerField(blank=False, null=False, choices = feature_choices, default=1)
    supported_fields = models.JSONField(blank=True, null=True, help_text = 'Format of each key, valae is NGBB_KEY: LIST_KEY where NGBB_KEY is the key used by NGBB and LIST_KEY is the key used by the list')
    api_path = models.TextField(blank=False, null=False, default="")

    class Meta:
        managed = False
        db_table = 'bot_list_api'

register(BotListApi)

class BotListFeature(models.Model):
    feature_id = models.IntegerField(primary_key = True)
    name = models.TextField(unique=True)
    iname = models.TextField(unique=True, verbose_name = "Internal Name")
    description = models.TextField(blank=True, null=True)
    positive = models.IntegerField(blank=False, null=False, choices = positive_choices)

    class Meta:
        managed = False
        db_table = 'bot_list_feature'

    def __str__(self):
        return self.name

register(BotListFeature)


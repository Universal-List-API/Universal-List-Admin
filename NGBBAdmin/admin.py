from django.contrib import admin
from django import forms
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from .config import *

class NGAdmin(SimpleHistoryAdmin):
    save_on_top = False
    search_fields = ('url',)

def url_f(obj):
    return obj.url

url_f.short_description = "Bot List URL"

def method_f(obj):
    return method[str(obj.method)]

method_f.short_description = "Method"

def endpoint_f(obj):
    return feature[str(obj.feature)]

endpoint_f.short_description = "Endpoint"

class BLAPI(NGAdmin):
    list_display = (url_f, endpoint_f, method_f)
# Register your models here.
admin.site.register(BotList, NGAdmin)
admin.site.register(BotListApi, BLAPI)

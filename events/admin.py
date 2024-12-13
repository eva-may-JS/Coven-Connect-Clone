from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_on', 'category')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


# Register your models here.

admin.site.register(Comment)
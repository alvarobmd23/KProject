from django.contrib import admin

from .models import Document_Type, Entry, EntryItem

admin.site.register(Document_Type)
admin.site.register(EntryItem)


class EntryItemInline(admin.TabularInline):
    model = EntryItem
    extra = 0


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    inlines = (EntryItemInline,)
    list_display = (
        '__str__',
        'employee',
        'company',
        'date',
        'document_type',
        'n_doc',
        'total_value',
    )
    search_fields = ('n_doc',)
    list_filter = ('employee',)
    date_hierarchy = 'created'

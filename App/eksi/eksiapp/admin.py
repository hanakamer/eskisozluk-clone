from django.contrib import admin

# Register your models here.

from .models import Title, Entry

class TitleAdmin(admin.ModelAdmin):
    fieldsets =[
        (None,                  {"fields" : ["title_text"]}),
        ("Date information",    {"fields" : ["pub_date"]}),
        ("Author",              {"fields" : ["author"]}),
    ]
    list_display = ("title_text", "author", "pub_date" )

    
class EntryAdmin(admin.ModelAdmin):
    fieldsets =[
        (None,                  {"fields" : ["entry_text"]}),
        ("Title",               {"fields" : ["title"]}),
        ("Author",              {"fields" : ["author"]}),

    ]
    list_display = ("title", "author", "entry_text", "pub_date_entry")


admin.site.register(Title, TitleAdmin )
admin.site.register(Entry, EntryAdmin)

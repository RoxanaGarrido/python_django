from django.contrib import admin
from tutorial.models import *

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'name', 'price', 'publisher', 'publish_date')
    list_filter = ('publisher__name',)
    search_fields = ('name',)
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)
    filter_horizontal = ('authors',)

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'foto')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Store)
admin.site.register(Fotografia, FotografiaAdmin)
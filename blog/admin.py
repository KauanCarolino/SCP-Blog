from django.contrib import admin

from blog.models import Publication, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'item_number',
        'object_class',
        'threat_level',
        'state_containment',
        'is_published',
        'author',
    )
    list_filter = ('object_class', 'threat_level', 'state_containment', 'is_published')
    search_fields = ('title', 'item_number', 'name_SCP', 'resume')
    list_editable = ('is_published',)
    autocomplete_fields = ('author', 'category')

from django.contrib import admin

from blog.models import Publication, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(Publication)
admin.site.register(Category, CategoryAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import AgentProfile


class AgentProfileInline(admin.StackedInline):
    model = AgentProfile
    can_delete = False
    verbose_name_plural = 'Perfil do Agente'
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    inlines = (AgentProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'clearance_level',
        'personnel_class',
        'site_assignment',
    )
    list_filter = ('clearance_level', 'personnel_class')
    search_fields = ('user__username', 'user__email', 'site_assignment')
    autocomplete_fields = ('user',)

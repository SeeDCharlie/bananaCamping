from django.contrib import admin
from django.contrib.auth.models import Group, PermissionManager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from .forms import *
from django.db.models import F


@admin.register(users)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    model = users

    list_display = ('email', 'nombre', 'apellido', 'tipo_usuario')
    list_display_links = ('email', 'nombre')
    list_filter = ('estado','tipo_usuario')

    fieldsets = (
        (None, {'fields': ('nickname', 'tipo_usuario', 'estado')}),
        ('Informacion personal', {'fields': ('email', 'no_documento', 'nombre', 'apellido', 'no_celular', 'tel_fijo','direccion', 'barrio','referencia_vivienda', 'password')}),
        ('Permisos', {'fields': ('groups' ,)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'tipo_usuario','no_documento', 'nombre', 'apellido', 'no_celular', 'tel_fijo','direccion', 'barrio', 'referencia_vivienda', 'estado', 'nickname', 'password1', 'password2'),
        }),
        ('Permisos', {'fields': ('groups',)}),
    )

    radio_fields = {"estado": admin.VERTICAL}

    search_fields = ('email', 'nombre', 'apellido')
    ordering = ('email','estado')
    filter_horizontal = ()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.tipo_usuario == type_user.objects.get(pk=1):
            return qs
        return qs.exclude(tipo_usuario=1).exclude(tipo_usuario = 2)

@admin.register(contact_request)
class solitudServAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'no_celular', 'fecha_solicitud', 'atendido' )
    #list_editable = ('atendido', )
    readonly_fields = ['email','nombre', 'no_celular', 'fecha_solicitud', 'mensaje']
    list_filter = ('atendido',)

admin.site.register(service)
admin.site.register(type_user)
admin.site.register(state_user)

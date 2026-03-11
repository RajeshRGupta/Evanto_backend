from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
# Register your models here.



class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email','first_name', 'last_name','phone']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name','phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email', 'first_name', 'last_name','phone')

class adminEventes(admin.ModelAdmin):
    list_display = ['image','user','title','details','genre','startDate','startTime','adderss','price','eventMode','language','age','deactivate']


class genreEventes(admin.ModelAdmin):
    list_display = ['user','categry']

class EventesCart(admin.ModelAdmin):
    list_display = ['events','quantity','user']


admin.site.register(User, UserAdmin)
admin.site.register(Eventes,adminEventes)
admin.site.register(Genre,genreEventes)
admin.site.register(Cart,EventesCart)
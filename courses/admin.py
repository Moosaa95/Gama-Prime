from django.contrib import admin
from .models import Programming, Business, Design, Management

# Register your models here.


@admin.register(Programming)
class ProgrammingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    list_filter = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    search_fields = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    list_filter = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    search_fields = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    list_filter = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    search_fields = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    list_filter = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    search_fields = ['name', 'description', 'image', 'create_at', 'update_at', 'is_enroll', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
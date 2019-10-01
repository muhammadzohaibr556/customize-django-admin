from django.contrib import admin
from .models import DemoProfile, CalculateField
from django.contrib.auth.models import User, Group 
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _ 
# Register your models here.
class MyUserAdmin(UserAdmin): 

    list_display = ("username","first_name", "last_name", "email","is_active","is_staff")
    list_filter = ()
    # Static overriding 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

class DemoProfileAdmin(admin.ModelAdmin):
    #actions_selection_counter = True
    #actions_on_bottom = False
    #actions_on_top = True

    fields = ('name', 'title','description', 'image', 'admin_photo')
    list_display = [
        'admin_photo',
        'name',
        'title',
        'short_description',
        'publish_date'
    ]
    list_display_links=[
        'name',
        'title'
    ]
    list_filter = [
        'name',
        'title',
        'publish_date'
    ]
    date_hierarchy = 'publish_date'
    
    readonly_fields = ('publish_date','admin_photo')
    

class CalculateFieldAdmin(admin.ModelAdmin):
    list_display = ['a', 'b', 'sum', 'subtract', 'multiply', 'divide']

    def sum(self, obj):
        return obj.a + obj.b
    
    def subtract(self, obj):
        return obj.a - obj.b
    
    def multiply(self, obj):
        return obj.a * obj.b

    def divide(self, obj):
        return obj.a / obj.b
    
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User,MyUserAdmin)
admin.site.register(DemoProfile, DemoProfileAdmin)
admin.site.register(CalculateField, CalculateFieldAdmin)
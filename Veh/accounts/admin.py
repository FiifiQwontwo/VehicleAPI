from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from carMake.models import VehicleMake
from django.utils.html import format_html
from fuel_type.models import Fuel

# Register your models here.

admin.site.site_header = "Vehicle API"
admin.site.site_title = "vehicle Admin"
admin.site.index_title = "Make"


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'last_login', 'date_joined')
    list_display_links = ('email', 'phone')
    readonly_fields = ('last_login', 'date_joined')
    # am ordering  date joined by descending order
    ordering = ('-date_joined',)
    # Used so the other required fields such as groups is disabled
    filter_horizontal = ()
    list_filter = ()
    # Used to make password read only
    fieldsets = ()


admin.site.register(Account, AccountAdmin)


@admin.register(VehicleMake)
class VehicleMakeAdmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html('<img src="{}" width="30" style="border_radius:50%;">'.format(object.logo.url))

    thumbnails.short_description = 'logo'
    list_display = ('thumbnails', 'make_name', 'created_at', 'updated_at',)
    list_display_links = ('make_name',)


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('fuel_type', 'created_at', 'updated_at',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.site_header = "Vehicle API"
admin.site.site_title = "vehicle Admin"
admin.site.index_title = "Make"


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'phone', 'last_login', 'date_joined')
    list_display_links = ('email', 'username', 'phone')
    readonly_fields = ('last_login', 'date_joined')
    # am ordering  date joined by descending order
    ordering = ('-date_joined',)
    # Used so the other required fields such as groups is disabled
    filter_horizontal = ()
    list_filter = ()
    # Used to make password read only
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
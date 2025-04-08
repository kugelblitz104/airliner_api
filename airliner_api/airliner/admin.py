from django.contrib import admin

from airliner.models import Address

class AddressAdmin(admin.ModelAdmin):
    fields = ['street_num', 'street_name', 'city', 'state', 'country', 'zip_code']
    list_filter = ['city', 'state', 'country']
    list_display = ['street_num', 'street_name', 'city', 'state', 'country']   
    search_fields = ['street_name', 'city', 'state', 'country']
    list_per_page = 100
    
admin.site.register(Address, AddressAdmin)
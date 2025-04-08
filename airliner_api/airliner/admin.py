from django.contrib import admin

import airliner.models as m
class AddressAdmin(admin.ModelAdmin):
    fields = ['street_num', 'street_name', 'city', 'state', 'country', 'zip_code']
    list_filter = ['city', 'state', 'country']
    list_display = ['street_num', 'street_name', 'city', 'state', 'country']   
    search_fields = ['street_name', 'city', 'state', 'country']
    list_per_page = 100
    

class AirportAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'address']
    list_display = ['name', 'code']
    search_fields = ['name', 'code']
    list_per_page = 100
    

class AirlineAdmin(admin.ModelAdmin):
    fields = ['name', 'code', 'country']
    list_filter = ['country']
    list_display = ['name', 'code']
    search_fields = ['name', 'code']
    list_per_page = 100
    

class PlaneModelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'manufacturer', 'exits', 'restrooms']}),
        ('Capacity', {'fields': ['crew_capacity', 'cockpit_crew_capacity', 'passenger_capacity'], 'classes': ['collapse']}),
        ('Performance', {'fields': ['range', 'max_speed', 'cruising_speed', 'fuel_capacity'], 'classes':['collapse']}),
        ('Dimensions', {'fields': ['weight', 'weight_capacity', 'length', 'wingspan', 'height'], 'classes':['collapse']}),
    ]
    list_filter = ['manufacturer']
    list_display = ['name', 'manufacturer', 'exits', 'restrooms']
    search_fields = ['name', 'manufacturer']
    list_per_page = 100
    
class PlaneAdmin(admin.ModelAdmin):
    fields = ['model', 'airline', 'registration_number', 'manufacture_date']
    list_filter = ['model__name', 'airline']
    list_display = ['registration_number', 'airport', 'model', 'airline', 'status']
    search_fields = ['registration_number', 'model__name', 'airline__name']
    list_per_page = 100

admin.site.register(m.Address, AddressAdmin)
admin.site.register(m.Airport, AirportAdmin)
admin.site.register(m.Airline, AirlineAdmin)    
admin.site.register(m.PlaneModel, PlaneModelAdmin)
admin.site.register(m.Plane, PlaneAdmin)
admin.site.register(m.Seat)
admin.site.register(m.Flight)
admin.site.register(m.Contact)
admin.site.register(m.Employee)
admin.site.register(m.Crew)
admin.site.register(m.Customer)
admin.site.register(m.Booking)
admin.site.register(m.Ticket)
from django.db import models
from django.contrib import admin

class Country(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']
        
class Address(models.Model):
    street_num = models.CharField(max_length=10, null=True, blank=True)
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)   
    state = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street_num} {self.street_name}, {self.city}, {self.state}, {self.country.name}, {self.zip_code}"
    
    class Meta:
        verbose_name_plural = 'Addresses'
        ordering = ['street_name', 'city']
    
class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
    class Meta:
        verbose_name_plural = 'Airports'
        ordering = ['code', 'name']
    
class Airline(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
    class Meta:
        verbose_name_plural = 'Airlines'
        ordering = ['name']

class PlaneModel(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    exits = models.IntegerField(null=True, blank=True)
    restrooms = models.IntegerField(null=True, blank=True)
    crew_capacity = models.IntegerField(help_text='not including cockpit crew', null=True, blank=True)
    cockpit_crew_capacity = models.IntegerField(help_text='not including flight attendants', null=True, blank=True)
    passenger_capacity = models.IntegerField(null=True, blank=True)
    range = models.DecimalField(help_text='kilometers', decimal_places=5, max_digits=13, null=True, blank=True)
    max_speed = models.DecimalField(help_text='km/h', decimal_places=5, max_digits=13, null=True, blank=True)
    cruising_speed = models.DecimalField(help_text='km/h', decimal_places=5, max_digits=13, null=True, blank=True)
    fuel_capacity = models.DecimalField(help_text='liters', decimal_places=5, max_digits=13, null=True, blank=True)
    weight = models.DecimalField(help_text='kg', decimal_places=5, max_digits=13, null=True, blank=True)
    weight_capacity = models.DecimalField(help_text='kg', decimal_places=5, max_digits=13, null=True, blank=True)
    length = models.DecimalField(help_text='meters', decimal_places=5, max_digits=13, null=True, blank=True)
    wingspan = models.DecimalField(help_text='meters', decimal_places=5, max_digits=13, null=True, blank=True)
    height = models.DecimalField(help_text='meters', decimal_places=5, max_digits=13, null=True, blank=True)
    length = models.DecimalField(help_text='meters', decimal_places=5, max_digits=13, null=True, blank=True)
    wingspan = models.DecimalField(help_text='meters', decimal_places=5, max_digits=13, null=True, blank=True)
    height = models.DecimalField(help_text='meters', decimal_places=5, max_digits=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.manufacturer})"
    
    @admin.display(description='Total Capacity')
    def total_capacity(self):
        return self.passenger_capacity or 0 + self.crew_capacity or 0 + self.cockpit_crew_capacity or 0
    
    class Meta:
        verbose_name_plural = 'Models'
        ordering = ['manufacturer', 'name']
          
class Plane(models.Model):
    model = models.ForeignKey(PlaneModel, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True, blank=True)
    airport = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    registration_number = models.CharField(max_length=10, unique=True)
    manufacture_date = models.DateField(null=True, blank=True)
    last_maintenance_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.airline.name} {self.model.name} ({self.registration_number})"
    
    class Meta:
        verbose_name_plural = 'Planes'
        ordering = ['airline', 'model']
    
class SeatType(models.Model):
    SEAT_TYPES = [
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first_class', 'First Class'),
    ]
    
    SEAT_POSITIONS = [
        ('aisle', 'Aisle'),
        ('window', 'Window'),
        ('middle', 'Middle'),
    ]
    
    type = models.CharField(max_length=50, choices=SEAT_TYPES, default='economy')
    position = models.CharField(max_length=50, choices=SEAT_POSITIONS, default='window')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} - {self.position}"
    
    class Meta:
        verbose_name_plural = 'Seat Types'
        ordering = ['type', 'position']
    
class Seat(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    seat_type = models.ForeignKey(SeatType, on_delete=models.RESTRICT)
    row = models.IntegerField()
    aisle = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.plane} - {self.seat_number}"
    
    class Meta:
        verbose_name_plural = 'Seats'
        ordering = ['plane', 'row', 'aisle']
    
class Flight(models.Model):
    flight_number = models.CharField(max_length=8)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_flights')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_flights')
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, null=True, blank=True)
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('delayed', 'Delayed'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.flight_number} - {self.departure_airport} to {self.arrival_airport}"
    
    class Meta:
        verbose_name_plural = 'Flights'
        ordering = ['flight_number']
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'
    
    class Meta:
        verbose_name_plural = 'Contacts'
        ordering = ['last_name', 'first_name']
    
class Employee(models.Model):
    EMPLOYEE_TYPES = [
        ('pilot', 'Pilot'),
        ('flight_attendant', 'Flight Attendant'),
        ('ground_staff', 'Ground Staff'),
        ('maintenance', 'Maintenance'),
    ]
    
    employee_type = models.CharField(max_length=50, choices=EMPLOYEE_TYPES, default='pilot')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.contact.first_name} {self.contact.last_name} - {self.employee_type}"
    
    class Meta:
        verbose_name_plural = 'Employees'
        ordering = ['contact__last_name', 'contact__first_name']

class Crew(models.Model):
    ROLE_TYPES = [
        ('pilot', 'Pilot'),
        ('co_pilot', 'Co-Pilot'),   
        ('flight_engineer', 'Flight Engineer'),
        ('cabin_crew', 'Cabin Crew'),
        ('lead_pilot', 'Lead Pilot'),
        ('first_officer', 'First Officer'),
        ('second_officer', 'Second Officer'),
        ('third_officer', 'Third Officer'),
        ('senior_flight_attendant', 'Senior Flight Attendant'),
        ('flight_attendant', 'Flight Attendant'),
        ('ground_staff', 'Ground Staff'),
    ]
    
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.flight} - {self.employee.contact.first_name}, {self.employee.contact.last_name} - {self.role}"
    
    class Meta:
        verbose_name_plural = 'Crew'
        ordering = ['flight', 'employee__contact__last_name', 'employee__contact__first_name']

class Customer(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    frequent_flyer_number = models.CharField(max_length=20, null=True, blank=True)
    loyalty_program = models.CharField(max_length=50, null=True, blank=True)
    accomodations = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.contact.first_name} {self.contact.last_name} - {self.frequent_flyer_number}"
    
    class Meta:
        verbose_name_plural = 'Customers'
        ordering = ['contact__last_name', 'contact__first_name']
    
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    confirmation_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.flight} - {self.seat}"
    
    class Meta:
        verbose_name_plural = 'Bookings'
        ordering = ['customer__contact__last_name', 'customer__contact__first_name']
                
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.booking} - {self.flight} - {self.seat}"
    
    class Meta:
        verbose_name_plural = 'Tickets'
        ordering = ['booking__customer__contact__last_name', 'booking__customer__contact__first_name']
    
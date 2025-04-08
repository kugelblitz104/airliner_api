from django.contrib.auth.models import Group, User
from rest_framework import serializers
import airliner.models as m

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Country
        fields = '__all__'
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Address
        fields = '__all__'

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Airport
        fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Airline
        fields = '__all__'

class PlaneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.PlaneModel
        fields = '__all__'
        
class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Plane
        fields = '__all__'
        
class SeatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.SeatType
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Seat
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Flight
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Contact
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Employee
        fields = '__all__'
        
class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Crew
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Customer
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Booking
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Ticket
        fields = '__all__'
        

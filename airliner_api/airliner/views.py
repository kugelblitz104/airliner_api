from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
import airliner.models as m
import airliner.serializers as s

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = s.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = s.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """
    queryset = m.Country.objects.all()
    serializer_class = s.CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be viewed or edited.
    """
    queryset = m.Address.objects.all()
    serializer_class = s.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class AirportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows airports to be viewed or edited.
    """
    queryset = m.Airport.objects.all()
    serializer_class = s.AirportSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class AirlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows airlines to be viewed or edited.
    """
    queryset = m.Airline.objects.all()
    serializer_class = s.AirlineSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PlaneModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows plane models to be viewed or edited.
    """
    queryset = m.PlaneModel.objects.all()
    serializer_class = s.PlaneModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class PlaneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows planes to be viewed or edited.
    """
    queryset = m.Plane.objects.all()
    serializer_class = s.PlaneSerializer
    permission_classes = [permissions.IsAuthenticated]

class SeatTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows seat types to be viewed or edited.
    """
    queryset = m.SeatType.objects.all()
    serializer_class = s.SeatTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SeatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows seats to be viewed or edited.
    """
    queryset = m.Seat.objects.all()
    serializer_class = s.SeatSerializer
    permission_classes = [permissions.IsAuthenticated]

class FlightViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flights to be viewed or edited.
    """
    queryset = m.Flight.objects.all()
    serializer_class = s.FlightSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = m.Contact.objects.all()
    serializer_class = s.ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = m.Employee.objects.all()
    serializer_class = s.EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CrewViewSet(viewsets.ModelViewSet):   
    """
    API endpoint that allows crews to be viewed or edited.
    """
    queryset = m.Crew.objects.all()
    serializer_class = s.CrewSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = m.Customer.objects.all()
    serializer_class = s.CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    queryset = m.Booking.objects.all()
    serializer_class = s.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    queryset = m.Ticket.objects.all()
    serializer_class = s.TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
    

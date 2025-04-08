"""
URL configuration for airliner_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from airliner import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'addresses', views.AddressViewSet)
router.register(r'airports', views.AirportViewSet)
router.register(r'airlines', views.AirlineViewSet)
router.register(r'planemodels', views.PlaneModelViewSet)
router.register(r'planes', views.PlaneViewSet)
router.register(r'seattype', views.SeatTypeViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'flights', views.FlightViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'crew', views.CrewViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'tickets', views.TicketViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
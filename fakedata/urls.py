from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from faker import Faker
# fake = Faker()
# fake.

fakedata_router = DefaultRouter()
fakedata_router.register(r"aadhar_number", viewset=AadharNumberViewSet, basename="aadhar_route")
fakedata_router.register(r"address", viewset=AddressViewSet, basename="address_route")
fakedata_router.register(r"email", viewset=EmailViewSet, basename="email_route")
fakedata_router.register(r"phone_number", viewset=PNViewSet, basename="pn_route")
fakedata_router.register(r"profile", viewset=ProfileViewSet, basename="profile_route")
fakedata_router.register(r"bank_name", viewset=BankViewSet, basename="bank_route")
fakedata_router.register(r"xml", viewset=XMLViewSet, basename="xml_route")


urlpatterns = [
    path("", include(fakedata_router.urls))
]

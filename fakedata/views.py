from locale import getdefaultlocale
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from faker import Faker
from rest_framework import status

MAX_LIMIT = 50


class AadharNumberViewSet(ViewSet):
    fake = Faker("en_IN")

    def list(self, request, *args, **kwargs):
        num = request.query_params.get("num", 5)

        try:
            num = int(num)
            if num > MAX_LIMIT:
                raise ValueError
        except ValueError:
            return Response({"message": "'num' parameter must be an integer and under 50"}, status=status.HTTP_400_BAD_REQUEST)

        aadhar_numbers = [self.fake.aadhaar_id() for _ in range(num)]
        return Response({"aadhar_numbers": aadhar_numbers})


class AddressViewSet(ViewSet):

    def list(self, request, *args, **kwargs):

        data = request.query_params
        locale = data.get("locale", getdefaultlocale()[0])
        num_address = data.get("num", 1)

        try:
            fake = Faker(locale=locale)
            num_address = int(num_address)
            if num_address > MAX_LIMIT:
                raise ValueError
        except ValueError:
            return Response({
                "message": "'num' should be positive integer and less than equal to 50"
            }, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            return Response({
                "message": "Please enter a valid locale"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = [fake.address() for _ in range(int(num_address))]

        return Response(data)


class EmailViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PNViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProfileViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class BankViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class XMLViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

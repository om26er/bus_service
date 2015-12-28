from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from bus_tracker.models import DriverModel
from bus_tracker.serializers import DriverSerializer


HIDDEN_PASSWORD_TEXT = '<HIDDEN>'


def get_user(username):
    try:
        return DriverModel.objects.get(username=username)
    except DriverModel.DoesNotExist:
        raise Http404


class DriverRegistrationView(APIView):

    def post(self, request, format=None):
        password = request.data.get('password')
        username = request.data.get('username')
        request.data.update({'password': HIDDEN_PASSWORD_TEXT})
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Update the password so that its hashed.
            user = DriverModel.objects.get(username=username)
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverLocationView(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, username, format=None):
        user = get_user(username)
        latitude = request.data.get('latitude', None)
        longitude = request.data.get('longitude', None)
        user.latitude = latitude
        user.longitude = longitude
        user.save()
        data = {"latitude": latitude, "longitude": longitude}
        return Response(data=data, status=status.HTTP_200_OK)

    def get(self, request, username, format=None):
        user = get_user(username)
        serializer = DriverSerializer(user)
        temp_data = serializer.data
        temp_data.update({'password': HIDDEN_PASSWORD_TEXT})
        return Response(data=temp_data, status=status.HTTP_200_OK)

from rest_framework import serializers

from bus_tracker.models import DriverModel


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = DriverModel
        fields = ('username', 'password', 'longitude', 'latitude',)

from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'date', 'photo']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'designation', 'specification', 'measurements']



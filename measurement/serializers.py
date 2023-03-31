from rest_framework import serializers
from .models import Measurement, Sensor


# class SerializatorSensor(serializers.Serializer):
#     name = serializers.CharField()
#     description = serializers.CharField()


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id_sensor', 'temperature', 'data_time']

class MeasurementSerializer_s(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'data_time']

class InfoSensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer_s(many=True, read_only=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']




# TODO: опишите необходимые сериализаторы

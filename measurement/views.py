# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement

from .serializers import SensorSerializer, MeasurementSerializer, InfoSensorSerializer


class Sensor_overview(ListAPIView):  ##класс отображения списка сенсоров
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        return Response({'POST': 'OK'})


class Sensor_view(RetrieveAPIView):  # класс отображения заданного сенсора
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class Sensor_update(RetrieveUpdateAPIView):  # класс изменения указанного сенсора  недоделан !!!!!!!!!!!
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class Sensor_all_info(RetrieveAPIView):  # класс отображения заданного сенсора со всеми измерениями
    queryset = Sensor.objects.all()
    serializer_class = InfoSensorSerializer


class Measurement_view(CreateAPIView):  # класс записи измерений сенсоров в бд
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class Sensor_create(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorSerializer


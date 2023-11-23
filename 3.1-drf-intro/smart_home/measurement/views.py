
from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics

from measurement.models import Sensor, Measurement

from measurement.serializers import SensorSerializer , SensorDetailSerializer, MeasurementSerializer

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer 


class MeasurementCreateAPIView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
     
 


# # TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# # TODO: ListCreateAPIView, RetrieveUpdateAPIView только с рк, CreateAPIView - только создает

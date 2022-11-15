# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView


from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        specification = self.request.data.get('specification')
        designation = self.request.data.get('designation')

        return serializer.save(specification=specification,
                               designation=designation)


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_update(self, serializer):
        specification = self.request.data.get('specification')
        designation = self.request.data.get('designation')

        return serializer.save(specification=specification,
                               designation=designation)


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = self.request.data.get('sensor_id')
        sensor_id = Sensor.objects.get(id=sensor)
        temperature = self.request.data.get('temperature')
        photo = self.request.data.get('photo')

        return serializer.save(sensor_id=sensor_id,
                               temperature=temperature,
                               photo=photo)

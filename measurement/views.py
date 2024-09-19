from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, \
    SensorDetailSerializer, SensorListSerializer


class CreateAPIView(ListAPIView):
    """Создать датчик.
    Указываются название и описание датчика."""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()
            print(review.data)
            print("OK create sensor")
        else:
            print(review.errors)
            print("Not OK create sensor")

        return Response({'status': 'OK'})


class ListView(ListAPIView):
    """Получить список датчиков.
    Выдается список с краткой информацией по датчикам:
    ID, название и описание"""
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class RetrieveUpdateAPIView(RetrieveAPIView):
    """Изменить информацию по конкретному датчику.
    ID, название, описание и список всех измерений
    с температурой и временем"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        """Изменить датчик.
        Указываются название и/или описание."""
        sensor = Sensor.objects.get(pk=pk)
        for key, value in sensor.__dict__.items():
            if key not in request.data:
                request.data[key] = value
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            print("OK")
        else:
            print(serializer.errors)
            print("Not OK")

        return Response(serializer.data)


class ListCreateAPIView(ListAPIView):
    """Добавить измерение.
    Указываются ID датчика и температура"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()
            print(review.data)
            print("OK create measurement")
        else:
            print(review.errors)
            print("Not OK create measurement")

        return Response({'status': 'OK'})

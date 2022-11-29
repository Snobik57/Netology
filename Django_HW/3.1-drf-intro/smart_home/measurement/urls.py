from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from measurement.views import SensorsView, SingleSensorView, MeasurementCreateView


urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>', SingleSensorView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.db import models


class Sensor(models.Model):

    designation = models.CharField(max_length=50)
    specification = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'sensor'
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):

    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='image', null=True)

    class Meta:
        db_table = 'measurement'
        verbose_name = 'измерение'
        verbose_name_plural = 'измерения'

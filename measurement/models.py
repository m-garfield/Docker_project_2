from django.db import models
class Sensor(models.Model):
     name = models.CharField(max_length=50)
     description = models.CharField(max_length=50)

class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(max_length=50)
    data_time = models.DateTimeField(max_length=50, auto_now=True)

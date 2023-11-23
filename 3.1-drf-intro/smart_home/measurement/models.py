from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length= 30, verbose_name= 'модель датчика')
    description = models.CharField(max_length= 50, verbose_name= 'расположение')

    def Meta():
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def _str_(self):
        return self.name

class Measurement(models.Model):
    
    temperature = models.IntegerField(verbose_name= 'температура')
    created_at = models.DateTimeField(auto_now_add= True, verbose_name= 'дата измерения') 
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')

    def Meta():
        verbose_name = 'Результат измерения'
        verbose_name_plural = 'Результаты измерений'

    def _str_(self):
        return self.sensor

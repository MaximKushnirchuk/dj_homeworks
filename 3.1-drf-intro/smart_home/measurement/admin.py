from django.contrib import admin
from measurement.models import Measurement, Sensor


class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name', 'description']

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'created_at', 'sensor']
    list_filter = ['id', 'temperature', 'created_at', 'sensor']


admin.site.register(Sensor, SensorAdmin)
admin.site.register(Measurement, MeasurementAdmin)
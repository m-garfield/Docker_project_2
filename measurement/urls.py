from django.urls import path

from measurement.views import Sensor_overview, Sensor_view, Measurement_view, Sensor_all_info, Sensor_update, \
    Sensor_create

urlpatterns = [
    path('sensors/<pk>/', Sensor_view.as_view()),
    path('measurement/', Measurement_view.as_view()),
    path('sensors-all-info/<pk>/', Sensor_all_info.as_view()),
    path('sensors-update/<pk>/', Sensor_update.as_view()),
    path('sensors-update/<pk>/', Sensor_update.as_view()),
    path('', Sensor_overview.as_view()),
    path('sensors/', Sensor_create.as_view()),


    # TODO: зарегистрируйте необходимые маршруты
]

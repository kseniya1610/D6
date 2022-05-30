from django.urls import path, include
from django.contrib import admin
from .views import AppointmentView, AppointView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AppointmentView.as_view(), name='make_appointment'),
    path('appoint/', AppointView.as_view(), name='test'),
]

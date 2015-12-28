from django.conf.urls import url

from bus_tracker.views import DriverRegistrationView, DriverLocationView


urlpatterns = [
    url(r'^api/drivers/register$', DriverRegistrationView.as_view()),
    url(r'^api/drivers/(?P<username>\w+)/location$',
        DriverLocationView.as_view())
]

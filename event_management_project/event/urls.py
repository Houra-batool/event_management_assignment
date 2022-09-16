from django.urls import path

from . views import *

#router = DefaultRouter()
#router.register(r'event', views.EventViewSet,basename="event")


urlpatterns = [
    path('all/', ListEvent.as_view()),
    path('add/', CreateEvent.as_view()),
    path('update/<int:pk>', UpdateEvent.as_view()),
    path('delete/<int:pk>', DeleteEvent.as_view()) ,
    path('attend/<int:pk>/', AttendEvent.as_view()), ]
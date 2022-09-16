from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path(r'^__debug__/', include(debug_toolbar.urls)),
]


   
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('draw/', include('draw.urls')),
    path('draw/custom/', include('draw.urls')),
]

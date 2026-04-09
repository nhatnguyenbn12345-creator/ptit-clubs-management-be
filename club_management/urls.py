from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('club_app.urls')), # Kết nối tới các API của club_app
]
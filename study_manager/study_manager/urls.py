# project_name/urls.py
from django.contrib import admin
from django.urls import path, include  # include is necessary for app URLs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Ensure this line is present

]

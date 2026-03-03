from django.contrib import admin
from django.urls import path, include
from tasks.views import register, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication endpoints
    path('api/register/', register),
    path('api/login/', login),
    path('api/logout/', logout),

    # Task endpoints
    path('api/', include('tasks.urls')),
]
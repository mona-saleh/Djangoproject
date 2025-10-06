from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page from bookmodule
    path('', include('apps.bookmodule.urls')),

    # User pages from usermodule
    path('users/', include('apps.usermodule.urls')),
]
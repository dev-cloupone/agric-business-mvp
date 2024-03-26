from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('fields/', include(('fields.urls', 'fields'), namespace='fields')),
    path('activities/', include(('activities.urls', 'activities'), namespace='activities')),
    path('supplies/', include(('supplies.urls', 'supplies'), namespace='supplies'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
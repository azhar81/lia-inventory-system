from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views
from users import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', authtoken_views.obtain_auth_token),
    path('', include('users.urls')),
    path('', include('vendors.urls')),
    path('', include('vendors.urls')),
    path('', include('assets.urls')),
    path('', include('locations.urls')),
    path('', include('lends.urls')),
    path('', include('inspections.urls')),
    path('', include('maintenances.urls')),
]

# Medias URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


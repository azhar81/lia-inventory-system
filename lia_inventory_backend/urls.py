from django.urls import include, path
from rest_framework import routers
from users import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('users.urls')),
    path('', include('vendors.urls')),
    path('', include('vendors.urls')),
    path('', include('assets.urls')),
    path('', include('locations.urls')),
    path('', include('lends.urls')),
]

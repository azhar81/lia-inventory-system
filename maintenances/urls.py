from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from maintenances import views

urlpatterns = [
  path('maintenances/', views.MaintenanceList.as_view()),
  path('maintenances/<int:pk>/', views.MaintenanceDetail.as_view()),
  path('maintenances/<int:pk>/approve', views.MaintenanceApprove.as_view()),
  path('maintenances/<int:pk>/reject', views.MaintenanceReject.as_view()),
  path('maintenances/<int:pk>/finish', views.MaintenanceFinish.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
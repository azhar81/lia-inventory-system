from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from vendors import views

urlpatterns = [
    path('vendors/', views.VendorList.as_view()),
    path('vendors/<int:pk>/', views.VendorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
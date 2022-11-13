from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lends import views

urlpatterns = [
  path('lends/', views.LendList.as_view()),
  path('lends/<int:pk>/', views.LendDetail.as_view()),
  path('lends/<int:pk>/return', views.LendReturn.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
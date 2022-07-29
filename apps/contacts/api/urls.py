from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ContactCreateAPIView.as_view()),
]

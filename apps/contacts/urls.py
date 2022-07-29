from django.urls import path, include
from .views import contact_view

app_name = 'contact'

urlpatterns = [
    path('', contact_view, name='contact'),

    path('api/', include('apps.contacts.api.urls')),
]

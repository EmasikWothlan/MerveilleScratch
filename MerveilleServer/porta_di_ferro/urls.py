from django.urls import path

from porta_di_ferro.views import porta_di_ferro, leave

urlpatterns = [
    path('', porta_di_ferro),
    path('leave/', leave)
]

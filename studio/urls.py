from django.urls import path
from .views import Index
from .views import OfferForm

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("date/", OfferForm.as_view(), name='date'),
]

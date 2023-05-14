from django.urls import path
from .views import Index
from .views import OfferForm
from .views import Book
from .views import Confirmation

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("date/", OfferForm.as_view(), name='date'),
    path("book/", Book.as_view(), name='book'),
    path("confirmation/", Confirmation.as_view(), name='confirmation'),

]

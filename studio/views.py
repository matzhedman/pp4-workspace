from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import OfferForm


# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'


class Book(TemplateView):
    template_name = 'book.html'



class OfferForm(CreateView):
    form_class = OfferForm
    template_name = 'date.html'
    success_url = '/'

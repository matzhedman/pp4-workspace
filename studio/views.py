from django.shortcuts import render

# Create your views here.


def get_studio_base(request):
    return render(request, 'studio/studio_base.html')

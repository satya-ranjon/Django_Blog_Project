from django.shortcuts import HttpResponseRedirect,render
from django.urls import reverse

def home (request):
    return HttpResponseRedirect(reverse('App_post:home'))

def handler404(request, exception):
    return render(request, '404.html')

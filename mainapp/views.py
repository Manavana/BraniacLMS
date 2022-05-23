#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello world!_ver2")


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")
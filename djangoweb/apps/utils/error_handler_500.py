from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, response


def custom_handler500(request, *args, **kwargs):
    return render(request, '500.html')

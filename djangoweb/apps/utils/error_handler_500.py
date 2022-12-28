from django.shortcuts import render


def custom_handler500(request, *args, **kwargs):
    return render(request, '500.html')

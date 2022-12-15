from django.http import HttpResponse
from django.template import loader, response


def custom_handler500(request, *args, **kwargs):
    template = loader.get_template('500.html')
    response.status_code = 500
    return HttpResponse(template.render(request))

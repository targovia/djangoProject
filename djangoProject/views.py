from django.http import HttpResponse


def message(request):
    return HttpResponse("Private Milen`s message for REST Framework purposes")

from django.http import HttpResponse

# Welcome Page
def welcome(request):
    return HttpResponse(
        'Welcome to the Tribune'
    )
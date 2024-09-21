from django.http  import HttpResponse

def new_home_page(request):
    return HttpResponse("Hello, World")

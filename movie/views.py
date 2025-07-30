from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a MovieReviews</h1>")

def about(request):
    return HttpResponse("<h1>Acerca de este proyecto</h1>")

from django.shortcuts import render        
# ↓ Ya no necesitamos HttpResponse

def home(request):
    return render(request, "movie/home.html")   

def about(request):
    return render(request, "movie/about.html")  


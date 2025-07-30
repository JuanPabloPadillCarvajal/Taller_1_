from django.contrib import admin
from django.urls import path
from movie import views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_views.home, name='home'),      # ruta raíz
    path('about/', movie_views.about, name='about'),  # /about
]

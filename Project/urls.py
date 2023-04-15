from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
    
    path("__reload__/", include("django_browser_reload.urls")),
]

from django.contrib import admin
from django.urls import path, include
# from myproject.views import bienvenido, tipopersona



urlpatterns = [
    path('admin/', admin.site.urls),
  
       path('principal/', include('principal.urls')  ),
       path('invernadero/', include('invernadero.urls')  ),
    
]
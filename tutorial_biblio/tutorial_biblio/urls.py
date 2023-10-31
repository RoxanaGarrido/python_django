"""tutorial_biblio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import tutorial.views
import tutorial_biblio.settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tutorial.views.index),
    path('galeria/', tutorial.views.galeria, name='galeria'),
    path('xml/', tutorial.views.librosxml, name='xml'),
    path('csv/', tutorial.views.libroscsv, name='csv'),
    path('pdf/', tutorial.views.librospdf, name='pdf'),
    path('json/', tutorial.views.librosjson, name='json'),
]

# si está en modo desarrollo usar esto para encontrar imágenes
if tutorial_biblio.settings.DEBUG:
    urlpatterns += static(tutorial_biblio.settings.MEDIA_URL, document_root=tutorial_biblio.settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from AppProyecto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('Blog.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

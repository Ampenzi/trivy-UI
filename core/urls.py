from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include


from authz.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authz.urls')),
    path('', index, name='index'),

] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")

admin.site.site_header = 'Trivy UI Admin Portal'
admin.site.site_title = 'Trivy  UI Admin Portal'  
admin.site.index_title = 'Trivy UI Admin Portal'



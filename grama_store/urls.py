from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('politica/', TemplateView.as_view(template_name='politica.html'), name='politica'),
    path('dicas/', TemplateView.as_view(template_name='dicas.html'), name='dicas'),
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='sobre'),
    # path('produtos/', include('produtos.urls')),  # Vamos criar depois
]

# Isso serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
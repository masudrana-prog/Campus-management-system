from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('academic/', include('academic.urls')),
    path('library/', include('library.urls')),
    path('social/', include('social.urls')),
    path('campus/', include('campus.urls')),
    path('dashboard/', include('users.dashboard_urls')),
    path('', RedirectView.as_view(url='/users/login/', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

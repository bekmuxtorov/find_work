from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from .schema import swagger_urlpatterns


def show_home(request):
    return render(request, 'index.html')


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),

    path('', show_home),
    path('api/', include('account.urls')),
    path('api/', include('work.urls')),
)

urlpatterns += swagger_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

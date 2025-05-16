from django.conf import settings
from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('api/v1/', include('apps.post.urls')),
    path('api/v1/', include('apps.comment.urls')),
    path('auth/', include('apps.user.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("admin/", admin.site.urls),

    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# # from apps.account import urls
# from apps.account import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.post.urls')),
    path('', include('apps.account.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

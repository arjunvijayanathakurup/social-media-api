from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("post.urls", namespace='post')),
]


# URL for accessing the images added to the urlpatterns
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

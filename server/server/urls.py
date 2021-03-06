from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^news/', include(('news.urls', 'news'), namespace='news')),
    re_path(r'^documents/', include(('docs.urls', 'docs'), namespace='docs')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

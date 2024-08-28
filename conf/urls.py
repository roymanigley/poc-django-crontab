from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core.views import CronLogView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logs/', CronLogView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

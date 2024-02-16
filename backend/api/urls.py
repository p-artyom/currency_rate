from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api.views import get_rate

urlpatterns = [
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema',
        ),
        name='swagger-ui',
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('rate/', get_rate),
]

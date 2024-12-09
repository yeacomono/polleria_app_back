from django.urls import path
from BACK.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.contrib import admin  # Importa el módulo admin
from django.urls import path, include  # Importa include para incluir las rutas de tus aplicaciones

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="CHAPITEC Eccomerce API",
        default_version='v1',
        description="Documentación para la API de Ecommerce",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="soporte@chapitec.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('accounts/login/', admin.site.urls),
    path('api/', include('BACK.urls')),
    # Swagger y Redoc
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Swagger y Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

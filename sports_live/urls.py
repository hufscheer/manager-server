from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework import permissions
from django.urls import include, path, re_path
from django.conf import settings

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="훕치치 매니저서버 API",
        default_version='v1',
        description="훕치치 매니저서버의 API 명세입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tsukiakarii@naver.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('games/', include("game.urls")),
    path('leagues/', include("league.urls")),
    path('reports/', include("report.urls")),
    path('league-teams/', include("team.urls")),
    path('timelines/', include("record.urls")),
    path('sports/', include("sport.urls")),
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
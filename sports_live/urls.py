from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('gane/', include("game.urls")),
    path('league/', include("league.urls")),
    path('report/', include("report.urls")),
    path('team/', include("team.urls")),
]

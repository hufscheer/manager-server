from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('games/', include("game.urls")),
    path('leagues/', include("league.urls")),
    path('reports/', include("report.urls")),
    path('teams/', include("team.urls")),
    path('timelines/', include("record.urls")),
    path('sports/', include("sport.urls")),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('game/', include("game.urls")),
    path('league/', include("league.urls")),
    path('report/', include("report.urls")),
    path('team/', include("team.urls")),
    path('record/', include("record.urls")),
    path('sport/', include("sport.urls")),
]

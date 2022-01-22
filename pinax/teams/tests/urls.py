from django.conf.urls import include, url

urlpatterns = [
    url(r"^account/", include("pinax.account.urls")),
    url(r"^", include("pinax.teams.urls", namespace="pinax_teams")),
]

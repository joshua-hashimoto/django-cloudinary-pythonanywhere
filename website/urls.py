from django.urls import path

from website.views import WebsiteListView, WebsiteDetailView, WebsiteCreateView


app_name = "website"

urlpatterns = [
    path("create/", WebsiteCreateView.as_view(), name="create"),
    path("<uuid:pk>/", WebsiteDetailView.as_view(), name="detail"),
    path("", WebsiteListView.as_view(), name="list"),
]

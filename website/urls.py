from django.urls import path

from website.views import WebsiteListView, WebsiteDetailView, WebsiteCreateView, WebsiteUpdateView


app_name = "website"

urlpatterns = [
    path("create/", WebsiteCreateView.as_view(), name="create"),
    path("<uuid:pk>/edit", WebsiteUpdateView.as_view(), name="update"),
    path("<uuid:pk>/", WebsiteDetailView.as_view(), name="detail"),
    path("", WebsiteListView.as_view(), name="list"),
]

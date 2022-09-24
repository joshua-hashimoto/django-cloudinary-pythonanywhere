from django.urls import path

from accounts.views import LoginAuthView, LogoutAuthView, SignUpAuthView

app_name = "accounts"

urlpatterns = [
    path("login/", LoginAuthView.as_view(), name="login"),
    path("logout/", LogoutAuthView.as_view(), name="logout"),
    path("signup/", SignUpAuthView.as_view(), name="signup"),
]

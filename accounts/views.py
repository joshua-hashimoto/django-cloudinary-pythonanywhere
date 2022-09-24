from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

from accounts.forms import CustomAuthenticationForm
from users.forms import CustomUserCreationForm


class LoginAuthView(LoginView):
    form_class = CustomAuthenticationForm
    template_name: str = "accounts/login.html"


class LogoutAuthView(View):

    def post(self, request):
        logout(request)
        url = reverse("website:list")
        return redirect(url)


class SignUpAuthView(CreateView):
    form_class = CustomUserCreationForm
    template_name: str = "accounts/signup.html"
    success_url = reverse_lazy("website:list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return redirect(self.get_success_url())

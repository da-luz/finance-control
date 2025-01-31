from django.contrib.auth.views import LoginView


class AuthLoginView(LoginView):
    template_name="authentication/login.html"
    next_page="/"

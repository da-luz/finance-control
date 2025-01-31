from django.urls import path

from authentication.views import AuthLoginView

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name="login"),
]

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class SignUpView(TemplateView):
    template_name = "signup.html"

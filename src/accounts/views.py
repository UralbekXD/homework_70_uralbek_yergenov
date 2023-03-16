from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import LoginForm


class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    form = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('index')

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect('index')

        login(request, user)
        next_page = request.GET.get('next')
        if next_page:
            return redirect(next_page)

        return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')

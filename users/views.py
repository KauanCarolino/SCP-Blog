# accounts/views.py
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.form import UserLoginForm, UserRegisterForm

class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Cadastro realizado com sucesso! Bem vindo Agente')
        return HttpResponseRedirect(self.request.path_info)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('blog:home')

    def get_success_url(self):
        return self.success_url

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

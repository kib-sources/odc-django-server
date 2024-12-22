"""
Основные views

Файл создан 08.10.2024 в 19:42:43

~/spotlightCramming/views.py
"""

__author__ = 'pavelmstu'
__copyright__ = 'KIB, 2024'
__license__ = 'LGPL'
__credits__ = [
    'pavelmstu',
]
__version__ = "20241019"
__status__ = "Develop"

# __status__ = "Production"

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import LoginForm, RegistrationForm
from django.urls import reverse_lazy

import os


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def example(request):
  template = loader.get_template('example.html')
  return HttpResponse(template.render())


class LoginView(FormView):
  template_name = 'login.html'
  form_class = LoginForm
  success_url = reverse_lazy('example')

  def form_valid(self, form) -> HttpResponse:
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(self.request, username=username, password=password)
    if user is not None:
      login(self.request, user)
      return super().form_valid(form)
    else:
      form.add_error(None, 'Неправильный логин или пароль')
      return self.form_invalid(form)


class RegisterView(FormView):
  template_name = 'register.html'
  form_class = RegistrationForm
  success_url = reverse_lazy('example')

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)
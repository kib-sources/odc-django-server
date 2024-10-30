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
from django.contrib.auth.decorators import login_required

import os


def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def example(request):
  template = loader.get_template('example.html')
  return HttpResponse(template.render())

@login_required(login_url='login')
def example(request):
    template = loader.get_template('example.html')
    return HttpResponse(template.render())
"""
Функции API

Файл создан 19.10.2024 в 12:24:58

~/odc_django_server/api.py
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


from django.http import JsonResponse


def ping(request):

    return JsonResponse(
        {
            "status": "ok"
        }
    )
# yourapp/__init__.py

from django.template import Library
from .custom_filters import get_value_from_dict

register = Library()

register.filter('get_value_from_dict', get_value_from_dict)

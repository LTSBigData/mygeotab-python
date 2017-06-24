# -*- coding: utf-8 -*-

__title__ = 'mygeotab-python'
__author__ = 'Aaron Toth'
__version__ = '0.5.4'

from .api import Credentials, MyGeotabException, AuthenticationException

try:
    from .async.api import API
except (SyntaxError, ImportError):
    from .api import API

__all__ = ['API', 'Credentials', 'MyGeotabException', 'AuthenticationException']
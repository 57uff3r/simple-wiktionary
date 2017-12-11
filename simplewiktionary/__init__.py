# -*- coding: utf-8 -*-
"""
    simple-wiktionary
    ~~~~~
    A python project which parses simple definitions of English words from  Wiktionary.
    :copyright: (c) 2017 by Andrey Korchak
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.1'

try:
    from .code import SimpleWiktionary
except ImportError:
    from code import SimpleWiktionary
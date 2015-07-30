import alias.classes
from alias.classes import *

import alias.inout
from alias.inout import *

import alias.semantics
from alias.semantics import *

import alias.exceptions
from alias.exceptions import *

""" Module that monkey-patches json module when it's imported so
JSONEncoder.default() automatically checks for a special "to_json()"
method and uses it to encode the object if found.
"""

# def _default(self, obj):
#     return getattr(obj.__class__, "to_json", _default.default)(obj)

# _default.default = JSONEncoder().default  # Save unmodified default.
# JSONEncoder.default = _default # replacement
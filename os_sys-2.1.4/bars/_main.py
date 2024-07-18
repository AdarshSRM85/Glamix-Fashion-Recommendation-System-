from .cli import *  # NOQA
from .cli import __all__  # NOQA
from .std import BarsDeprecationWarning
from warnings import warn
warn("This function will be removed in bars==5.0.0\n"
     "Please use `bars.cli.*` instead of `bars._main.*`",
     BarsDeprecationWarning, stacklevel=2)

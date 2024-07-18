from .std import *  # NOQA
from .std import __all__  # NOQA
from .std import BarsDeprecationWarning
from warnings import warn
warn("This function will be removed in bars==5.0.0\n"
     "Please use `bars.std.*` instead of `bars._bars.*`",
     BarsDeprecationWarning, stacklevel=2)

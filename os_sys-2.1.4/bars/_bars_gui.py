from .gui import *  # NOQA
from .gui import __all__  # NOQA
from .std import BarsDeprecationWarning
from warnings import warn
warn("This function will be removed in bars==5.0.0\n"
     "Please use `bars.gui.*` instead of `bars._bars_gui.*`",
     BarsDeprecationWarning, stacklevel=2)

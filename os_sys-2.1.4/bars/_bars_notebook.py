from .notebook import *  # NOQA
from .notebook import __all__  # NOQA
from .std import BarsDeprecationWarning
from warnings import warn
warn("This function will be removed in bars==5.0.0\n"
     "Please use `bars.notebook.*` instead of `bars._bars_notebook.*`",
     BarsDeprecationWarning, stacklevel=2)

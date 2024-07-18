from .std import *  # NOQA
from .std import __all__  # NOQA
from .std import BarsDeprecationWarning
from warnings import warn
warn("This function will be removed in tqdm==5.0.0\n"
     "Please use `tqdm.std.*` instead of `tqdm._tqdm.*`",
     BarsDeprecationWarning, stacklevel=2)

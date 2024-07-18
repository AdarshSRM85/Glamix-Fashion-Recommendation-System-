from .std import tqdm, brange
from .gui import tqdm as tqdm_gui  # TODO: remove in v5.0.0
from .gui import brange as tgrange  # TODO: remove in v5.0.0
from ._tqdm_pandas import tqdm_pandas
from .cli import main  # TODO: remove in v5.0.0
from ._monitor import TMonitor, BarsSynchronisationWarning
from ._version import __version__  # NOQA
from .std import BarsTypeError, BarsKeyError, BarsWarning, \
    BarsDeprecationWarning, BarsExperimentalWarning, \
    BarsMonitorWarning

__all__ = ['tqdm', 'tqdm_gui', 'brange', 'tgrange', 'tqdm_pandas',
           'tqdm_notebook', 'tnrange', 'main', 'TMonitor',
           'BarsTypeError', 'BarsKeyError',
           'BarsWarning', 'BarsDeprecationWarning',
           'BarsExperimentalWarning',
           'BarsMonitorWarning', 'BarsSynchronisationWarning',
           '__version__']


def tqdm_notebook(*args, **kwargs):  # pragma: no cover
    """See tqdm.notebook.tqdm for full documentation"""
    from .notebook import tqdm as _tqdm_notebook
    from warnings import warn
    warn("This function will be removed in tqdm==5.0.0\n"
         "Please use `tqdm.notebook.tqdm` instead of `tqdm.tqdm_notebook`",
         BarsDeprecationWarning, stacklevel=2)
    return _tqdm_notebook(*args, **kwargs)


def tnrange(*args, **kwargs):  # pragma: no cover
    """
    A shortcut for `tqdm.notebook.tqdm(xrange(*args), **kwargs)`.
    On Python3+, `range` is used instead of `xrange`.
    """
    from .notebook import brange as _tnrange
    from warnings import warn
    warn("Please use `tqdm.notebook.brange` instead of `tqdm.tnrange`",
         BarsDeprecationWarning, stacklevel=2)
    return _tnrange(*args, **kwargs)

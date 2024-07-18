from .std import bars, brange
from .gui import bars as bars_gui  # TODO: remove in v5.0.0
from .gui import brange as tgrange  # TODO: remove in v5.0.0
from ._bars_pandas import bars_pandas
from .cli import main  # TODO: remove in v5.0.0
from ._monitor import TMonitor, BarsSynchronisationWarning
from ._version import __version__  # NOQA
from .std import BarsTypeError, BarsKeyError, BarsWarning, \
    BarsDeprecationWarning, BarsExperimentalWarning, \
    BarsMonitorWarning

__all__ = ['bars', 'bars_gui', 'brange', 'tgrange', 'bars_pandas',
           'bars_notebook', 'tnrange', 'main', 'TMonitor',
           'BarsTypeError', 'BarsKeyError',
           'BarsWarning', 'BarsDeprecationWarning',
           'BarsExperimentalWarning',
           'BarsMonitorWarning', 'BarsSynchronisationWarning',
           '__version__']


def bars_notebook(*args, **kwargs):  # pragma: no cover
    """See bars.notebook.bars for full documentation"""
    from .notebook import bars as _bars_notebook
    from warnings import warn
    warn("This function will be removed in bars==5.0.0\n"
         "Please use `bars.notebook.bars` instead of `bars.bars_notebook`",
         BarsDeprecationWarning, stacklevel=2)
    return _bars_notebook(*args, **kwargs)


def tnrange(*args, **kwargs):  # pragma: no cover
    """
    A shortcut for `bars.notebook.bars(xrange(*args), **kwargs)`.
    On Python3+, `range` is used instead of `xrange`.
    """
    from .notebook import brange as _tnrange
    from warnings import warn
    warn("Please use `bars.notebook.brange` instead of `bars.tnrange`",
         BarsDeprecationWarning, stacklevel=2)
    return _tnrange(*args, **kwargs)

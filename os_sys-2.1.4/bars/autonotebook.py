import os

try:
    from IPython import get_ipython
    if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
        raise ImportError("console")
    if 'VSCODE_PID' in os.environ:  # pragma: no cover
        raise ImportError("vscode")
except:
    from .std import bars, brange
else:  # pragma: no cover
    from .notebook import bars, brange
    from .std import BarsExperimentalWarning
    from warnings import warn
    warn("Using `bars.autonotebook.bars` in notebook mode."
         " Use `bars.bars` instead to force console mode"
         " (e.g. in jupyter console)", BarsExperimentalWarning, stacklevel=2)
__all__ = ["bars", "brange"]

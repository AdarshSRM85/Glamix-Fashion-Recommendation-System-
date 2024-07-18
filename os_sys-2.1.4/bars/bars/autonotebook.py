import os

try:
    from IPython import get_ipython
    if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
        raise ImportError("console")
    if 'VSCODE_PID' in os.environ:  # pragma: no cover
        raise ImportError("vscode")
except:
    from .std import tqdm, brange
else:  # pragma: no cover
    from .notebook import tqdm, brange
    from .std import BarsExperimentalWarning
    from warnings import warn
    warn("Using `tqdm.autonotebook.tqdm` in notebook mode."
         " Use `tqdm.tqdm` instead to force console mode"
         " (e.g. in jupyter console)", BarsExperimentalWarning, stacklevel=2)
__all__ = ["tqdm", "brange"]

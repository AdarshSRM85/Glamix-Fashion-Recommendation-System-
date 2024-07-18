import warnings
from .std import BarsExperimentalWarning
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=BarsExperimentalWarning)
    from .autonotebook import bars, brange
__all__ = ["bars", "brange"]

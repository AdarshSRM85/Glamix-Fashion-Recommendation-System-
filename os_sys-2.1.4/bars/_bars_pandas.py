import sys

__author__ = "github.com/casperdcl"
__all__ = ['bars_pandas']


def bars_pandas(tclass, *targs, **tkwargs):
    """
    Registers the given `bars` instance with
    `pandas.core.groupby.DataFrameGroupBy.progress_apply`.
    It will even close() the `bars` instance upon completion.

    Parameters
    ----------
    tclass  : bars class you want to use (eg, bars, bars_notebook, etc)
    targs and tkwargs  : arguments for the bars instance

    Examples
    --------
    >>> import pandas as pd
    >>> import numpy as np
    >>> from bars import bars, bars_pandas
    >>>
    >>> df = pd.DataFrame(np.random.randint(0, 100, (100000, 6)))
    >>> bars_pandas(bars, leave=True)  # can use bars_gui, optional kwargs, etc
    >>> # Now you can use `progress_apply` instead of `apply`
    >>> df.groupby(0).progress_apply(lambda x: x**2)

    References
    ----------
    https://stackoverflow.com/questions/18603270/
    progress-indicator-during-pandas-operations-python
    """
    from bars import BarsDeprecationWarning

    if isinstance(tclass, type) or (getattr(tclass, '__name__', '').startswith(
            'bars_')):  # delayed adapter case
        BarsDeprecationWarning("""\
Please use `bars.pandas(...)` instead of `bars_pandas(bars, ...)`.
""", fp_write=getattr(tkwargs.get('file', None), 'write', sys.stderr.write))
        tclass.pandas(*targs, **tkwargs)
    else:
        BarsDeprecationWarning("""\
Please use `bars.pandas(...)` instead of `bars_pandas(bars(...))`.
""", fp_write=getattr(tclass.fp, 'write', sys.stderr.write))
        type(tclass).pandas(deprecated_t=tclass)

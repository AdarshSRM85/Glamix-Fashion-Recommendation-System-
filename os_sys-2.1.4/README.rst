.. |pypi| image:: https://img.shields.io/pypi/v/progress.svg
   :target: https://pypi.org/project/progress/
.. |demo| image:: https://raw.github.com/verigak/progress/master/demo.gif
   :alt: Demo

include:

    introduction
    
    sorry                                                                                  
    	
    description                                                                                                                                                                    
    	
    license(at the end)
    home
    loading_bars

introduction:


    to install os_sys you type: pip install os_sys                                                                                  
    to upgrade os_sys you type: pip install --upgrade os_sys                                                                                  
    so lets get start to install os_sys                                                                                  

sorry:                                                                                  
    i am dutch and i never had a mind about it while become this far so some commands are in dutch.                                                                                  
    the most commands are english but sorry if you not understand some commands.                                                                                  
    the most new packages and update's while be in english                                                                                  

discription:                                                                                  
    os_sys is a extra package for python(3)                                                                                  
    it's a extra to have a more easy use of the normal python libs                                                                                  
    plz look sometimes to my packages becuse i am making more own libs(extra is not that own lib)                                                                                  
    if i have more info i while show it here                                                                                   
    plz read the license                                                                                  
    
    



license:
    Copyright (c) 2018 The Python Packaging Authority

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
loading_bars:
Easy progress reporting for Python
==================================




|pypi|

|demo|


Bars
----

There are 7 progress bars to choose from:

- ``Bar``
- ``ChargingBar``
- ``FillingSquaresBar``
- ``FillingCirclesBar``
- ``IncrementalBar``
- ``PixelBar``
- ``ShadyBar``

To use them, just call ``next`` to advance and ``finish`` to finish:

.. code-block:: python

    from os_sys.progress import bar

    bar = Bar('Processing', max=20)
    for i in range(20):
        # Do some work
        bar.next()
    bar.finish()

or use any bar of this class as a context manager:

.. code-block:: python

    from os_sys.progress import bar

    with Bar('Processing', max=20) as bar:
        for i in range(20):
            # Do some work
            bar.next()

The result will be a bar like the following: ::

    Processing |#############                   | 42/100

To simplify the common case where the work is done in an iterator, you can
use the ``iter`` method:

.. code-block:: python

    for i in Bar('Processing').iter(it):
        # Do some work

Progress bars are very customizable, you can change their width, their fill
character, their suffix and more:

.. code-block:: python

    bar = Bar('Loading', fill='@', suffix='%(percent)d%%')

This will produce a bar like the following: ::

    Loading |@@@@@@@@@@@@@                   | 42%

You can use a number of template arguments in ``message`` and ``suffix``:

==========  ================================
Name        Value
==========  ================================
index       current value
max         maximum value
remaining   max - index
progress    index / max
percent     progress * 100
avg         simple moving average time per item (in seconds)
elapsed     elapsed time in seconds
elapsed_td  elapsed as a timedelta (useful for printing as a string)
eta         avg * remaining
eta_td      eta as a timedelta (useful for printing as a string)
==========  ================================

Instead of passing all configuration options on instatiation, you can create
your custom subclass:

.. code-block:: python

    class FancyBar(Bar):
        message = 'Loading'
        fill = '*'
        suffix = '%(percent).1f%% - %(eta)ds'

You can also override any of the arguments or create your own:

.. code-block:: python

    class SlowBar(Bar):
        suffix = '%(remaining_hours)d hours remaining'
        @property
        def remaining_hours(self):
            return self.eta // 3600


Spinners
========

For actions with an unknown number of steps you can use a spinner:

.. code-block:: python

    from os_sys.progress import spinner

    spinner = Spinner('Loading ')
    while state != 'FINISHED':
        # Do some work
        spinner.next()

There are 5 predefined spinners:

- ``Spinner``
- ``PieSpinner``
- ``MoonSpinner``
- ``LineSpinner``
- ``PixelSpinner``
home:
    plz visit my one website there you can post evry program for python that you want:
    https://python-libs-com.webnode.nl/

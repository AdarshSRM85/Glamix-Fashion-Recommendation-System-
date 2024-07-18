import os
def _setup():
    exec(open('..\commands\__init__.py').read(), globals())
    setup_os_sys()
_setup()

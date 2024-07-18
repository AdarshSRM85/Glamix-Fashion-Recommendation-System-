"""
ChatterBot is a machine learning, conversational dialog engine.
default is the default path to the db learning file
indev you create a new file so you can see how it works
"""
from .chatterbot import ChatBot
import os
from distutils.sysconfig import get_python_lib as gpl
path = gpl()
default = 'sqlite://' + os.path.join(os.path.dirname(__file__),'database.sqlite3').replace('\\','/')
indev = 'sqlite:///database.sqlite3'

__all__ = (
    'ChatBot','default','indev'
)

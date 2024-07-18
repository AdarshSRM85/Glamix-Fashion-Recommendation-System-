from time import strftime
import sys, os
import subprocess
import platform
from os import linesep
from time import sleep
from enum import IntEnum
import platform
from datetime import datetime
import psutil
from abc import ABCMeta, abstractmethod
from collections.abc import MutableMapping, Container
import socket
from datetime import timedelta, datetime
import netifaces as nif
from threading import Timer
import re
from collections.abc import Callable
from functools import partial
from os import path
loggers = {}
def print_hr(space_before=False, space_after=False):
    before = linesep if space_before else ''
    after = linesep if space_after else ''
    print(before + '-' * 80 + after)





#-----------------------gui printer---------------------

from tkinter import *
from tkinter import scrolledtext
import sys
# Run tkinter code in another thread

import tkinter as tk
import threading

class GUI_APLOCATION():

    def __init__(self,mainloop=False,thread=True):
        if thread:
            threading.Thread.__init__(self)
        self.root = tk.Tk()
        
        
        self.root.geometry("800x600")

        self.canvas = scrolledtext.ScrolledText(self.root)
        self.canvas.tag_config('warning', foreground="red")
        self.canvas.tag_config('normal', foreground='blue')
        self.canvas.place(x=0,y=0,width=800,height=600)
        self.canvas.config(state=DISABLED)
        
        self.do_mainloop = mainloop
        self.updated = False
        self.do_thread = thread
        if thread:
            self.start()
        

    def callback(self):
        self.root.quit()

    def run(self):
        self.started = True
        if self.do_mainloop == True:
            self.root.mainloop()
        else:
            import time
            while True:
                if self.updated == True:
                    kwargs = self.up_kwargs
                    msg = self.up_msg
                    while self.updated == True:
                        try:
                            self.canvas.config(state=NORMAL)
                            global y
                            msg = list(msg)
                            for i in range(0,len(msg)):
                                msg[i] = str(msg[i])
                            try:
                                sep = kwargs['sep']
                            except:
                                sep = ''
                            if isset(kwargs,'file'):
                                if kwargs['file'] == sys.stderr:
                                    red = True
                            else:
                                red = False
                            self.canvas.insert(END,sep.join(msg), 'warning' if red else 'normal')
                            self.canvas.insert(END,'\n')
                            self.canvas.config(state=DISABLED)
                            self.canvas.update_idletasks()
                            self.updated = False
                            self.up_msg = None
                            self.up_kwargs = None
                        except:
                            pass
                try:
                    self.root.update()
                except:
                    pass
                
    def print(self, *msg,**kwargs):
        if self.do_thread:
            self.updated=True
            self.up_msg = msg
            self.up_kwargs = kwargs
        else:
            self.canvas.config(state=NORMAL)
            global y
            msg = list(msg)
            for i in range(0,len(msg)):
                msg[i] = str(msg[i])
            try:
                sep = kwargs['sep']
            except:
                sep = ''
            if isset(kwargs,'file'):
                if kwargs['file'] == sys.stderr:
                    red = True
                else:
                    red = False
            else:
                red = False
            self.canvas.insert(END,sep.join(msg), 'warning' if red else 'normal')
            self.canvas.insert(END,'\n')
            self.canvas.config(state=DISABLED)
            self.canvas.update_idletasks()
            self.canvas.update()
            self.updated = False
            self.up_msg = None
            self.up_kwargs = None

GUI_APLOCATIO = GUI_APLOCATION


def isset(dictory,key):
    try:
        dictory[key]
        return True
    except:
        return False
my_old_printer = print


y = 0
def print_(*msg,**kwargs):
    GUI_APLOCATIO.canvas.config(state=NORMAL)
    global y
    msg = list(msg)
    for i in range(0,len(msg)):
        msg[i] = str(msg[i])
    try:
        sep = kwargs['sep']
    except:
        sep = ''
    if isset(kwargs,'file'):
        if kwargs['file'] == sys.stderr:
            red = True
    else:
        red = False
    GUI_APLOCATIO.canvas.insert(END,sep.join(msg), 'warning' if red else 'normal')
    GUI_APLOCATIO.canvas.insert(END,'\n')
    GUI_APLOCATIO.canvas.config(state=DISABLED)
    GUI_APLOCATIO.canvas.update_idletasks()
    #GUI_APLOCATIO.root.update()
def show_GUI():
    GUI_APLOCATIO.root.update_idletasks()
    GUI_APLOCATIO.root.deiconify()
    GUI_APLOCATIO.root.update_idletasks()
    #root.update()
def hide_GUI():
    GUI_APLOCATIO.root.withdraw()
    
def PrintOnGUI():
    global print
    globals().update({'print':print_})
    GUI_APLOCATIO.root.update_idletasks()
    GUI_APLOCATIO.root.deiconify()
    GUI_APLOCATIO.root.update_idletasks()
    
    #root.update()
    print = print_
def print_normal():
    global print,my_old_printer
    globals().update({'print':my_old_printer})
    print = my_old_printer
    GUI_APLOCATIO.root.withdraw()
#---------get logger---------
def get_logger(name):
    try:
        return loggers[f'os_sys-logger-{name}']
    except:
        try:
            return globals()[f'{name}']
        except:
            print(f'WARNING: logger {name} is not found returning None',file=sys.stderr)
            return None
#---------add logger---------
def add_logger(name,logger):
    loggers[f'os_sys-logger-{name}'] = logger
    globals().update({f'{name}': logger})
    
#############################################################
#                                                           #
#                    the loggers                            #
#                  by Matthijs Labots                       #
#                                                           #
#############################################################
#----------basic logger-----------
#this is the basic format for all the other loggers
class basic_logger():
    def __init__(self,name,debug=False,counter=False,costum_format=None,make_file=False):
        """start the logger if debug is false debug messages wont be showed you can change the debug setteng by calling basic_logger.config(debug=True or False)"""
        self.counter = counter
        self.count = 0
        count = '{count}'
        self.Debug = debug
        if counter == True:
            self.raw_format = f"{count}: [%Y-%m-%d %H:%M:%S]: module: {name}" if costum_format==None else costum_format.format_map({'name': name})
        else:
            self.raw_format = f"[%Y-%m-%d %H:%M:%S]: module: {name}" if costum_format==None else costum_format.format_map({'name': name})
        self.make_file = make_file
        add_logger(name,self)
        if self.make_file:
            self.file = open(f'{name}.log', 'w+')
    def format(self,change=None):
        """if change = none:
        returns the format
        else:
        change the raw_format"""
        if change == None:
            return strftime(self.raw_format)
        else:
            self.raw_format = change
            return self.format()
    def set_debug(self, debug):
        self.Debug=debug
    def config(self, debug):
        self.Debug=debug
    def conf(self, **kwargs):
        change = ['debug']
        for i in list(kwargs):
            if i in change:
                exec(f'self.{i} = {kwargs[i]}',globals(),locals())
            else:
                self.warn(f'{i} is not a argument')
                
                
    def info(self,msg,*f_args,**f_kwargs):
        msg = str(msg)
        self.count += 1
        if self.count == True:
            f_kwargs['count'] = self.count
        print(self.format(),str(msg % f_args).format_map(f_kwargs),sep=': ',flush=True)
        if self.make_file:
            self.file.write(f'INFO: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
    def debug(self,msg,*f_args,**f_kwargs):
        self.count += 1
        msg = str(msg)
        if self.count == True:
            f_kwargs['count'] = self.count
        if self.Debug == False:
            return
        print('DEBUG:', self.format()+':',str(msg % f_args).format_map(f_kwargs),file=sys.stderr,flush=True)
        if self.make_file:
            self.file.write(f'DEBUG: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
    def warning(self,msg,*f_args,**f_kwargs):
        self.count += 1
        msg = str(msg)
        if self.count == True:
            f_kwargs['count'] = self.count
        
        print('WARNING:', self.format()+':',str(msg % f_args).format_map(f_kwargs),file=sys.stderr,flush=True)
        if self.make_file:
            self.file.write(f'WARNING: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
    def warn(self,msg,*f_args,**f_kwargs):
        
        self.warning(msg,*f_args,**f_kwargs) 
    def log(self,msg,level,*f_args,**f_kwargs):
        msg = str(msg)
        """log with level:
        1: info
        2: debug
        3: warning
        4: error
        5: fatal error
        """
        try:
            level = int(level)
        except:
            self.warning(f'expected an int got an {type(level)}')
            return
        if level == 1:
            self.info(msg,*f_args,**f_kwargs)
        elif level == 2:
            self.debug(msg,*f_args,**f_kwargs)
        elif level == 3:
            self.warning(msg,*f_args,**f_kwargs)
        elif level == 4:
            self.error(msg, fatal=False,*f_args,**f_kwargs)
        elif level == 5:
            self.error(msg,fatal = True, *f_args,**f_kwargs)
        else:
            self.warning(f'expected an int between 1 and 5 got number {level}')
        
    def error(self,msg, fatal=False,exit_fatal=False,*f_args,**f_kwargs):
        self.count += 1
        msg = str(msg)
        if self.count == True:
            f_kwargs['count'] = self.count
        if fatal == True:
            fatal1 = 'FATAL '
        else:
            fatal1 = ''
        print(f'{fatal1}ERROR: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}',file=sys.stderr,flush=True)
        if self.make_file:
            self.file.write(f'{fatal1}ERROR: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
        if fatal == True and exit_fatal == True:
            try:
                self.file.close()
            except:
                pass
            raise SystemExit

#---------file logger------------
class file_logger(basic_logger):
    def __init__(self,name,debug=False,costum_format=None):
        """start the logger if debug is false debug messages wont be showed you can change the debug setteng by calling basic_logger.config(debug=True or False)"""
        self.Debug = debug
        self.raw_format = f"[%Y-%m-%d %H:%M:%S] module: {name}" if costum_format==None else costum_format
        self.make_file = True
        add_logger(name,self)
        if self.make_file:
            self.file = open(f'log.os_sys_log', 'w+')
#---------the normal logger class-----------
class Logger(basic_logger):
    def __init__(self,name,debug=False,costum_format=None,make_file=False):
        """start the logger if debug is false debug messages wont be showed you can change the debug setteng by calling basic_logger.config(debug=True or False)"""
        self.Debug = debug
        self.raw_format = f"[%Y-%m-%d %H:%M:%S] module: {name}" if costum_format==None else costum_format
        self.make_file = make_file
        add_logger(name,self)
        if self.make_file:
            self.file = open(f'{name}.log', 'w+')
    def add_logger(self,logger,name, *f_args,**f_kwargs):
        """logger: a log function or class, name=how you want to call the function, how to call a function:
        logger.{name} then you have your logger"""
        
                
        exec(f"self.{name} = logger", globals(),locals())
    def show(self,msg,insert,*f_args,**f_kwargs):
        print(str(str(self.format() if insert==True else '')+':'),str(msg % f_args).format_map(f_kwargs),flush=True)
    def title(self,title,msg=None,*f_args,**f_kwargs):
        msg = str(msg)
        print('-'*30,str(title),'-'*30,sep='')
        if msg!=None:
            print(self.format(),"INFO",str(msg % f_args).format_map(f_kwargs),sep=': ',flush=True)
            if self.make_file:
                self.file.write(f'INFO: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
                self.file.flush()
                os.fsync(self.file.fileno())
            
    def startup(self,msg,*f_args,**f_kwargs):
        msg = str(msg)
        
        print(self.format(),"startup info",str(msg % f_args).format_map(f_kwargs),sep=': ',flush=True)
        if self.make_file:
            self.file.write(f'INFO: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
#----------test class-------------
class Test(Logger):
    def __init__(self,name,debug=True,costum_format=None,make_file=False):
        """start the logger if debug is false debug messages wont be showed you can change the debug setteng by calling basic_logger.config(debug=True or False)"""
        self.Debug = debug
        self.raw_format = f"[%Y-%m-%d %H:%M:%S] module: {name}" if costum_format==None else costum_format
        self.make_file = make_file
        self.exceptions = []
        self.errors = []
        self.warnings = []
        self.succes = []
        self.wrong = []
        self.tests = []
        add_logger(name,self)
        if self.make_file:
            self.file = open(f'test-{name}.os_sys_log', 'w+')
    def eq(self,value1,value2,test_name=''):
        if value1 == value2:
            self.info(f'test {test_name}: succes')
            if test_name != '':
                test_name = test_name + ' '
            self.succes.append(f'test {test_name}:{value1} == {value2}: True')
            self.tests.append(f'test {test_name}:{value1} == {value2}: True')
            return True
        else:
            self.warn(f'test {test_name}: error')
            self.wrong.append(f'test {test_name}:{value1} == {value2}: False')
            self.tests.append(f'test {test_name}:{value1} == {value2}: False')
            return False

class gui_logger(GUI_APLOCATION):
    def __init__(self,name,debug=False,costum_format=None,make_file=True):
        """start the logger if debug is false debug messages wont be showed you can change the debug setteng by calling basic_logger.config(debug=True or False)"""
        self.Debug = debug
        thread=False
        self.raw_format = f"[%Y-%m-%d %H:%M:%S] module: {name}" if costum_format==None else costum_format
        self.make_file = make_file
        add_logger(name,self)
        if self.make_file:
            self.file = open(f'{name}.log', 'w+')
        GUI_APLOCATION.__init__(self,mainloop,thread)
    def add_logger(self,logger,name, *f_args,**f_kwargs):
        """logger: a log function or class, name=how you want to call the function, how to call a function:
        logger.{name} then you have your logger"""
        
                
        exec(f"self.{name} = logger", globals(),locals())
    def show(self,msg,insert,*f_args,**f_kwargs):
        self.print(str(str(self.format() if insert==True else '')+':'),str(msg % f_args).format_map(f_kwargs),flush=True)
    def title(self,title,msg=None,*f_args,**f_kwargs):
        msg = str(msg)
        self.print('-'*30,str(title),'-'*30,sep='')
        if msg!=None:
            self.print(self.format(),"INFO",str(msg % f_args).format_map(f_kwargs),sep=': ',flush=True)
            if self.make_file:
                self.file.write(f'INFO: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
                self.file.flush()
                os.fsync(self.file.fileno())
            
    def startup(self,msg,*f_args,**f_kwargs):
        msg = str(msg)
        
        self.print(self.format(),"startup info",str(msg % f_args).format_map(f_kwargs),sep=': ',flush=True)
        if self.make_file:
            self.file.write(f'INFO: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
    def format(self,change=None):
        """if change = none:
        returns the format
        else:
        change the raw_format"""
        if change == None:
            return strftime(self.raw_format)
        else:
            self.raw_format = change
            return self.format()
    def set_debug(self, debug):
        self.Debug=debug
    def config(self, debug):
        self.Debug=debug
    def conf(self, **kwargs):
        change = ['debug']
        for i in list(kwargs):
            if i in change:
                exec(f'self.{i} = {kwargs[i]}',globals(),locals())
            else:
                self.warn(f'{i} is not a argument')
                
                
    def info(self,msg,*f_args,**f_kwargs):
        msg = str(msg)
        self.print(self.format(),str(msg % f_args).format_map(f_kwargs),sep=': ',flush=True)
        if self.make_file:
            self.file.write(f'INFO: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
    def debug(self,msg,*f_args,**f_kwargs):
        msg = str(msg)
        if self.Debug == False:
            return
        self.print('DEBUG:', self.format()+':',str(msg % f_args).format_map(f_kwargs),file=sys.stderr,flush=True)
        if self.make_file:
            self.file.write(f'DEBUG: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
    def warning(self,msg,*f_args,**f_kwargs):
        msg = str(msg)
        
        self.print('WARNING:', self.format()+':',str(msg % f_args).format_map(f_kwargs),file=sys.stderr,flush=True)
        if self.make_file:
            self.file.write(f'WARNING: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
    def warn(self,msg,*f_args,**f_kwargs):
        
        self.warning(msg,*f_args,**f_kwargs) 
    def log(self,msg,level,*f_args,**f_kwargs):
        msg = str(msg)
        """log with level:
        1: info
        2: debug
        3: warning
        4: error
        5: fatal error
        """
        try:
            level = int(level)
        except:
            self.warning(f'expected an int got an {type(level)}')
            return
        if level == 1:
            self.info(msg,*f_args,**f_kwargs)
        elif level == 2:
            self.debug(msg,*f_args,**f_kwargs)
        elif level == 3:
            self.warning(msg,*f_args,**f_kwargs)
        elif level == 4:
            self.error(msg, fatal=False,*f_args,**f_kwargs)
        elif level == 5:
            self.error(msg,fatal = True, *f_args,**f_kwargs)
        else:
            self.warning(f'expected an int between 1 and 5 got number {level}')
        
    def error(self,msg, fatal=False,exit_fatal=False,*f_args,**f_kwargs):
        msg = str(msg)
        if fatal == True:
            fatal1 = 'FATAL '
        else:
            fatal1 = ''
        self.print(f'{fatal1}ERROR: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}',file=sys.stderr,flush=True)
        if self.make_file:
            self.file.write(f'{fatal1}ERROR: {self.format()}: {str(msg % f_args).format_map(f_kwargs)}\n')
            self.file.flush()
            os.fsync(self.file.fileno())
        if fatal == True and exit_fatal == True:
            try:
                self.file.close()
            except:
                pass
            raise SystemExit
__all__ = 'basic_logger,file_logger,Logger,Test,gui_logger'.split(',')
#the test


def test():
    logger = gui_logger(__name__)
    logger.startup('succes starting tests now')
    logger.info('test')
    logger.info(logger)
    logger.debug('nothing')
    logger.add_logger(file_logger('test'), 'test')
    logger.test.info('test: logger')
    logger.test.log('test level 3', '3')
    logger.config(debug=True)
    logger.info('normal')
    print(get_logger(__name__))
    try:
        get_logger(__name__).info('this is from get logger')
    except:
        pass
    #expiriment tests
    #PrintOnGUI()
    logger.info('GUI')
    logger.warn('warning')
    logger.startup('succes')
    import time
    time.sleep(1)
    #print_normal()
    logger.warning('not normal')
    logger.info('normal again')
    logger.info('showing GUI for one second')
    #show_GUI()
    time.sleep(1)
    #hide_GUI()
    logger.log('again a test',1)
    logger.log('test int converter', '1')
    logger.log('test no int found warning', 'lol')
    logger.log('test to high int warning', 6)
    logger.log('test to low int warning', -1)
    logger.debug('error next')
    #PrintOnGUI()
    logger.error('no fatal error')
    time.sleep(1)
    #print_normal()
    logger.error('fatal error', fatal=True, exit_fatal=True)
    logger.info('lol')
    
if __name__ == '__main__':
    test()

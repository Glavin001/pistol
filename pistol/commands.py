#!/usr/bin/env python
__author__ = '''
Dawson Reid (dreid93@gmail.com)
'''
import logging

class init(object):

    def __init__(self):
        self.logger = logging.getLogger('{0}'.format(self))

    def __call__(self, args):
        self.logger.info('Initializing the package.yaml.')
        self.logger.debug(args)

        import string

        tamplate = string.Template('''
        
        ''')




class install(object):

    def __init__(self):
        pass

    def __call__(self, args):
        pass


class uninstall(object):

    def __init__(self):
        pass

    def __call__(self, args):
        pass

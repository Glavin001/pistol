#!/usr/bin/env python
__author__ = '''
Dawson Reid (dreid93@gmail.com)
'''
import logging

def query_yes_no(question):
    answer = raw_input('{0} (y/N) : '.format(question)).lower()
    return answer[:1] == 'y'

def query_string(question, default):
    answer = raw_input(question)
    return default if answer == '' else answer


class init(object):

    def __init__(self):
        self.logger = logging.getLogger('{0}'.format(self))

    def __call__(self, args):
        self.logger.info('Initializing the package.yaml.\n')

        package = {
            'name': query_string('name ({0}) : '.format(args.name), args.name),
            'version': raw_input('version ({0}) : '.format(args.version)),
            'description': raw_input('description ({0}) : '.format(args.description)),
            'authors': [],
            'keywords': [],
            'bin': []
            'dependencies': {
                'common': []
            }
        }

        # add authors
        add_author = query_yes_no('\nWould you like to add an author?')
        while add_author:
            author = {
                'name': raw_input('name : '),
                'email': raw_input('email : '),
                'uri': raw_input('uri : ')
            }
            package['authors'].append(author)

            add_author = query_yes_no('Would you like to add another author?')

        # add keywords
        add_keywords = query_yes_no('\nWould you like to add a keyword?')
        while add_keywords:
            keyword = raw_input('keyword : ')
            package['keywords'].append(keyword)

            add_keyword = query_yes_no('Would you like to add another keyword?')


        self.logger.info('Done build the package.yaml.\n')

        f = open('package.yaml', 'w')
        import yaml
        yaml.dump(package, f, default_flow_style=False)
        f.close()


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

#!/usr/bin/env python
__author__ = '''
Dawson Reid (dreid93@gmail.com)
'''
import logging, sys
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG)

import argparse

parser = argparse.ArgumentParser(
    prog='pistol',
    description='A Python package manager that shoots from the hip!',)

subparsers = parser.add_subparsers(
    title='pistol',
    description='',
    prog='pistol',
    help='help help help')

import commands

init_parser = subparsers.add_parser('init',
    help='Initialize and empty pistol project.')
init_parser.set_defaults(func=commands.init())

def project_name():
    import os 
    current_dir = os.path.dirname(__file__)
    project_name = current_dir.split('/')[-1:][0]
    return project_name

init_parser.add_argument('--name', default=project_name())
init_parser.add_argument('--version')
init_parser.add_argument('--author')
init_parser.add_argument('--description')
init_parser.add_argument('--keyword')
init_parser.add_argument('--bin')


install_parser = subparsers.add_parser('install',
    help='Install packages as specified within the package.yaml file.')
install_parser.set_defaults(func=commands.install())


uninstall_parser = subparsers.add_parser('uninstall',
    help='')
uninstall_parser.set_defaults(func=commands.uninstall())

args = parser.parse_args()
args.func(args)

import os

basedir = os.path.dirname(__file__)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'buka-umbulaka'



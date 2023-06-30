from subprocess import Popen
from time import strftime


now = strftime('%Y%m%d%H%M%S')
args = ['py',  '-Xutf8', 'manage.py', 'dumpdata', '>', f'backup_{now}.json']

Popen(args, shell=True)

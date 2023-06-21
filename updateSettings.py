# -*- coding: utf-8 -*-
"""修改settings.py DEBUG为False"""
import re
import sys
import subprocess

print('Starting updating settings.py')
print('Script location:' + __file__)
print('Start to read settings.py')
# read
with open('ShareAndTalk/settings.py', encoding='utf-8') as f:
    lines = f.readlines()
print('Read successfully')
print('Start to modify')
# modify
for index, line in enumerate(lines):
    if re.match(r'^DEBUG', line):
        if lines[index] == 'DEBUG = False\n':
            print('No need to modity')
            print('program ends')
            sys.exit()
        else:
            lines[index] = 'DEBUG = False\n'
# write
with open('ShareAndTalk/settings.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Modify successfully')

print('Start to commit')
# run git
commands = [
    ['git', 'config', '--global', 'user.name', 'Skyler Sun'],
    ['git', 'config', '--global', 'user.email', '3385213313@qq.com'],
    ['git', 'add', '.'],
    ['git', 'commit', '-m', 'Update settings.py'],
    ['git', 'push', 'origin', 'HEAD:main'],
]

for cmd in commands:
    subprocess.Popen(cmd).wait()

print('Program ends')

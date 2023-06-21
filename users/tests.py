"""users tests"""
# set environment vars
import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShareAndTalk.settings')
setup()
# import
from django.test import TestCase

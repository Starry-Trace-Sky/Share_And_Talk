"""api test"""
# set environment vars
import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ShareAndTalk.settings')
setup()
# import
import unittest
from hashlib import md5
from django.urls import reverse
from django.core import mail
from django.conf import settings
from django.test import TestCase

from api.views import getQQAvatarLink
from users.models import Profile

class TestAPI(TestCase):
    """test app api"""
    def updateUser(self):
        self.user = Profile.objects.get(id=self.user.id)
    
    def setUp(self):
        # init setting
        settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
        self.qqAccount = '3385213313'
        self.gravatarAccount = '3385213313@qq.com'
        self.user = Profile.objects.create(nickname='a')
        self.client.force_login(self.user)
        
    def testGravatarPhoto(self):
        """test gravatar photo"""
        response = self.client.post(reverse('api:GravatarPhoto'),
                                    {'Gravatar': self.gravatarAccount}, 
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        
        self.updateUser()
        md = md5(self.gravatarAccount.encode()).hexdigest()
        self.assertEqual(self.user.avatar, 
                         f'https://sdn.geekzu.org/avatar/{md}?size=40')
        self.assertEqual(response.content.decode(), 'ok')

    def testSendEmail(self):
        response = self.client.post(reverse('api:send_email'),
                                    {'message': 'test1'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertRedirects(response, reverse('blog:pages'))

from django.test import TestCase, Client
from django.test.testcases import SimpleTestCase
from django.core.files.base import ContentFile

from LegacySite.models import User, Product
from.views import *

#https://docs.djangoproject.com/en/3.2/topics/testing/overview/
#note: need to rename test
class testattack1(TestCase)
    def setupClient(self):
        self.client = Client()     
    
    def testcrosssite(self):
        response = self.client.get('/buy.html?director=<script>alert('xxs')</script>attacked%211')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<script>alert('xxs')</script>attacked!1!', count=None, status_code=200, html=False)
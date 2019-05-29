from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import test, reverse
from django.utils.translation import ugettext_lazy as __
import httpretty
from django.contrib.sites.models import Site
import json
import requests



class AccountSocialAccountTest(APITestCase):
	def setUp(self):
		'''
		Setting up the new site for the new default application
		'''
		httpretty.enable()
	def _domain_information_pull_with_json(self, provider):
		return json.dumps(
			{
			"code":"oofgawd",
			"redirect_uri":('http://{}{}').format(Site.objects.get_current().domain, reverse.reverse('account-social-login', args=(provider,))),
			"provider":provider
			}
			)	
	def test_social_account_with_no_valid_provider(self):
		'''
		Testing the instance of a foreign backend
		'''
		provider='facebook'
		resp = self.client.get(reverse.reverse('account-social-login', args=(provider,)))
		print(resp.data)
		self.assertEqual(resp.status_code, 500)
		self.assertEqual(resp.data['detail'], __('Missing Backend'))

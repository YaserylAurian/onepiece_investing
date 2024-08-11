"""Tests of the sign up view"""
from django.test import TestCase
from django.urls import reverse
from stocks.forms import SignUpForm
from stocks.models import User
from django.contrib.auth.hashers import check_password

class SignUpViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('sign_up')
        self.form_input = {
            "username": "johndoe",
            "new_password": "Password123",
            "password_confirmation": "Password123"
        }
        self.response_url = reverse('home')


    def test_sign_up_url(self):
        self.assertEqual(self.url, '/sign_up/')

    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertFalse(form.is_bound)

    def test_unsuccesful_sign_up(self):
        self.form_input['username'] = ''
        before_count = User.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, SignUpForm))
        self.assertTrue(form.is_bound)

    def test_succesful_sign_up(self):
        before_count = User.objects.count()
        response = self.client.post(self.url, self.form_input, follow=True)
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count+1)
        self.assertRedirects(response, self.response_url, status_code = 302, target_status_code=200)
        self.assertTemplateUsed(response, 'home.html')
        user = User.objects.get(username='johndoe')
        self.assertTrue(check_password('Password123', user.password))
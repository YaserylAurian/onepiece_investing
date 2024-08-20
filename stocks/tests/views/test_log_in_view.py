from django.test import TestCase
from django.urls import reverse
from stocks.forms import LogInForm

class LogInViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('log_in')
        self.response_url = reverse('home')


    def test_sign_up_url(self):
        self.assertEqual(self.url, '/log_in/')
    
    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
from django.test import TestCase
from django.urls import reverse
from stocks.forms import LogInForm
from stocks.models import User

class LogInViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('log_in')
        self.response_url = reverse('home')
        self.form_input = {
            'username' : 'johndoe',
            'password' : 'Password123'}
        User.objects.create_user(
            username='johndoe', 
            password='Password123'
            )
    
    def _is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()

    def test_sign_up_url(self):
        self.assertEqual(self.url, '/log_in/')
    
    def test_get_sign_up(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
    
    def test_unsuccesful_log_in(self):
        self.form_input['password'] = 'WrongPassword123'
        response = self.client.post(self.url, self.form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LogInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self._is_logged_in())

    def test_succesful_log_in(self):
        response = self.client.post(self.url, self.form_input, follow=True)
        self.assertRedirects(response, self.response_url, status_code = 302, target_status_code=200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTrue(self._is_logged_in())
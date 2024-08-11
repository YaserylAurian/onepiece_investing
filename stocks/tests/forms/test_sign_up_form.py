"""Unit tests of the sign up form"""
from django.test import TestCase
from django import forms
from django.contrib.auth.hashers import check_password
from stocks.forms import SignUpForm
from stocks.models import User

class SignUpFormTestCase(TestCase):

    def setUp(self):
        self.form_input = {
            "username": "johndoe",
            "new_password": "Password123",
            "password_confirmation": "Password123"
        }

    def test_valid_sign_up_form(self):
        
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    
    def test_form_has_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('username', form.fields)
        self.assertIn('new_password', form.fields)
        self.assertIn('password_confirmation', form.fields)

    def test_password_field_widget(self):
        form = SignUpForm()
        new_password_widget = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))

        password_confirm_widget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(password_confirm_widget, forms.PasswordInput))

    def test_form_uses_model_validation(self):
        self.form_input['username'] = 'b'*31
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    
    def test_new_password_and_password_confirmation_are_indentical(self):
        self.form_input['password_confirmation'] = "WrongPassword123"
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_must_save_correctly(self):
        form = SignUpForm(data=self.form_input)
        before_count = User.objects.count()
        form.save()
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count+1)
        user = User.objects.get(username='johndoe')
        self.assertTrue(check_password('Password123', user.password))
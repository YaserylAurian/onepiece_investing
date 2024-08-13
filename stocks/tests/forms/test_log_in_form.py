"""Unit tests of the log in form"""
from django.test import TestCase
from django import forms
from django.contrib.auth.hashers import check_password
from stocks.forms import SignUpForm
from stocks.models import User

class LogInFormTestCase(TestCase):
    pass
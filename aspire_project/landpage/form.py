from datetime import date
from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.forms.extras.widgets import Select, SelectDateWidget
from django.forms.widgets import EmailInput
from django.conf import settings
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
    )
    captcha = CaptchaField()


# Captcha Setup:
# http://django-simple-captcha.readthedocs.org/en/latest/usage.html#installation
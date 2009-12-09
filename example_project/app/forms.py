from django import forms
from math_captcha.forms import MathCaptchaModelForm
from models import Model

class Form(MathCaptchaModelForm):
    class Meta:
        model = Model
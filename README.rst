Simple Math Captcha
=========================

:Authors:
   Justin Quick <justquick@gmail.com>
:Version: 0.1

Django Math Captcha is an easy way to add mathematical captcha verification to your already existing forms.
It asks you a simple math question (eg ``'1 + 2 ='``) and validates the form if your response is correct.
All you have to do is subclass either ``MathCaptchaForm`` or ``MathCaptchaModelForm`` in your own forms.

Use it in your forms::

    from math_captcha import MathCaptchaModelForm
    from myapp.models import Blog

    class MyExistingForm(MathCaptchaModelForm): # instead of forms.ModelForm
        #... extra fields here
        
        class Meta:
            model = Blog
            

Now you can be certain that the only users who create blogs are humans

Check out the example project for more practical use and tests.

Settings
---------

Set the behavior of the math captcha interaction in your settings.py

``MATH_CAPTCHA_NUMBERS``

A list of numbers to randomly choose from when generating the questions.
Defaults to ``[1,2,3,4,5]``.

``MATH_CAPTCHA_OPERATORS``

List of mathematical operators to use. Default is only add (``+``) and subtract (``-``).
Available operators are: add (``+``), subtract (``-``), multiply (``*``), divide (``/``), and modulo (``%``)

``MATH_CAPTCHA_QUESTION``

Question that appears on forms as a label for math questions. By default it is ``'Are you human?'``

Simple Math Captcha
=========================

:Authors:
   Justin Quick <justquick@gmail.com>
:Version: 0.1

Django Math Captcha is an easy way to add mathematical captcha verification to your already existing forms.
It asks you a simple math question (eg ``'1 + 2 ='``) and validates the form if your response is correct.
All you have to do is subclass either ``MathCaptchaForm`` or ``MathCaptchaModelForm`` in your own forms.

Extending your forms::

    from math_captcha import MathCaptchaModelForm
    from myapp.forms import BlogForm

    class MyExistingForm(BlogForm,MathCaptchaModelForm): # instead of forms.ModelForm
        #... extra fields here
            

Now you can be certain that the only users who create blogs are humans. 

Check out the example project for more practical use and tests.

Using with other apps
----------------------

If you are running an app like, say `django-contact-form`_ and want to add math captcha here is how to go about it.

Add the following in your ``urls.py``::

    from contact_form.forms import ContactForm
    from math_captcha.forms import MathCaptchaForm
    
    class CaptchaContactForm(ContactForm,MathCaptchaForm):
        pass
        
    urlpatterns = patterns('',
        ...
        url(r'^contact/$','contact_form.views.contact_form',{'form_class':CaptchaContactForm},name='contact_form'),
        url(r'^contact/sent/$','django.views.generic.simple.direct_to_template',{ 'template': 'contact_form/contact_form_sent.html' },name='contact_form_sent'),
        ...
    )
    
Now the contact form will block robots who cant do math.

.. _django-contact-form: http://bitbucket.org/ubernostrum/django-contact-form

Settings
---------

Set the behavior of the math captcha interaction in your ``settings.py``

``MATH_CAPTCHA_NUMBERS = (1,2,3,4,5)``

A list of numbers to randomly choose from when generating the questions.
Defaults to 1 through 5.

``MATH_CAPTCHA_OPERATORS = '+-'``

String containing mathematical operators to use. Default is only add (``+``) and subtract (``-``).
Available operators are: add (``+``), subtract (``-``), multiply (``*``), divide (``/``), and modulo (``%``)

``MATH_CAPTCHA_QUESTION = 'Are you human?'``

Question that appears on forms as a label for math questions. By default it is ``'Are you human?'``

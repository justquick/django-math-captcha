from django.db import models

class Model(models.Model):
    field = models.TextField(help_text='Im a text field',blank=True,null=True)
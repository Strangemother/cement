from django import forms
from trim.forms import fields


class VeryForm(forms.Form):
    subject = fields.chars(max_length=255, required=False) #
    sender = fields.email(required=False)
    cc_myself = fields.bool_false()
    message = fields.text(required=True)
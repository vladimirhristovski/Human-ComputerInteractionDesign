from django import forms
from .models import *


class EstateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EstateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['reserved', 'sold']:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Estate
        fields = '__all__'

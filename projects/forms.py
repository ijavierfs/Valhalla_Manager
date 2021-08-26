from datetime import datetime

from django import forms
from .models import Project, ProjectPermission

"""
Constants
"""
ERROR_MESSAGE_TITLE = {'required': 'El título es un campo obligatorio', 'unique': 'El título ya existe', 'invalid': 'El título no es válido'}

"""
Classes
"""
class ProjectForm (forms.ModelForm):
    title = forms.CharField( label = 'Título', required=True, error_messages=ERROR_MESSAGE_TITLE)
    description = forms.CharField( label = 'Description', required=True, widget = forms.Textarea )
    dead_line = forms.DateField(initial=datetime.now)

    class Meta:
        model = Project
        fields = ('title', 'description', 'dead_line')

class PermissionProjectForm(forms.Form):
    permission = forms.ModelChoiceField(queryset=ProjectPermission.objects.all(), initial=0)

    def __init__(self, *args, **kwargs):
        super(PermissionProjectForm, self).__init__(*args, **kwargs)
        self.fields['permission'].widget.attrs.update({'class': 'browser-default'})

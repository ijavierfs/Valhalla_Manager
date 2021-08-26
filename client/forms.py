from django import forms
from django.contrib.auth.models import User

from client.models import Client, SocialNetwork

"""
Constants
"""
ERROR_MESSAGE_USER = {'required': 'El password es requerido', 'unique': 'El usuario ya existe', 'invalid': 'El usuario no es válido'}
ERROR_MESSAGE_PASS = {'required': 'El password es requerido'}
ERROR_MESSAGE_MAIL = {'required': 'El email es requerido', 'invalid': 'El correo introducido no es válido'}

"""
Functions
"""

def must_be_gt_5(value_password):
    if len(value_password) < 5:
        raise forms.ValidationError('El password debe ser mayor de 4 caracteres')

"""
Classes
"""

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget = forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'username_login', 'class': 'input_login'})
        self.fields['password'].widget.attrs.update({'id': 'password_login', 'class': 'input_login'})

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_USER)
    password = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_PASS, widget=forms.PasswordInput(), validators=[must_be_gt_5])
    email = forms.CharField(error_messages=ERROR_MESSAGE_MAIL)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id': 'username_register', 'class': ''})
        self.fields['password'].widget.attrs.update({'id': 'password_register', 'class': ''})
        self.fields['email'].widget.attrs.update({'id': 'email_register', 'class': ''})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count():
            raise forms.ValidationError('El email debe ser unico')
        return email

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class EditUserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, error_messages=ERROR_MESSAGE_USER, label="Usuario")
    email = forms.CharField(error_messages=ERROR_MESSAGE_MAIL, label="Email")
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellidos')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.id).count():
            raise forms.ValidationError('El email debe ser unico')
        return email

class EditPasswordForm(forms.Form):
    old_password = forms.CharField(max_length=20, label='Contraseña actual', widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=20, label='Contraseña nueva', widget=forms.PasswordInput(),validators=[must_be_gt_5])
    rep_password = forms.CharField(max_length=20, label='Repetir Contraseña nueva',widget=forms.PasswordInput(),validators=[must_be_gt_5])

    def clean(self):
        clean_data = super(EditPasswordForm, self).clean()
        password1 = clean_data['new_password']
        password2 = clean_data['rep_password']

        if password1 != password2:
            raise forms.ValidationError('Las passwords no son iguales')

class EditClientForm (forms.ModelForm):
    job = forms.CharField (label = "Trabajo actual", required= False)
    bio = forms.CharField (label = "Biografía",  required= False, widget=forms.Textarea)
    class Meta:
        model = Client
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(EditClientForm, self).__init__(*args, **kwargs)
        self.fields['job'].widget.attrs.update({'id':'job_edit_client', 'class': 'validate'})
        self.fields['bio'].widget.attrs.update({'id':'bio_edit_client', 'class': 'validate'})

class EditClientSocial(forms.ModelForm):
    class Meta:
        model = SocialNetwork
        exclude = ['user']
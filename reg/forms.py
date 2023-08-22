from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Parent


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

PROVINCES = (
    ('', 'Choose province...'),
    ('AB', 'Alberta'),
    ('BC', 'British Columbia'),
    ('MB', 'Manitoba'),
    ('NB', 'New Brunswick'),
    ('NL', 'Newfoundland and Labrador'),
    ('NS', 'Nova Scotia'),
    ('ON', 'Ontario'),
    ('PEI', 'Prince Edward Island'),
    ('QC', 'Quebec'),
    ('SK', 'Saskatchewan')
)


class AddParentForm(forms.Form):
    fn = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}), label="First name", max_length=100, required=True)
    ln = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}), label="Last name", max_length=100, required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    cell = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '519-555-1212'}))
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )

    city = forms.CharField()
    province = forms.ChoiceField(choices=PROVINCES)
    postal_code = forms.CharField(label='Postal code', widget=forms.TextInput(attrs={'placeholder': 'N6H5L2'}))
    wants_email = forms.BooleanField(label='Send YAPCA-related emails to this parent\'s address')


class EditParentForm(forms.Form):
    fn = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}), label="First name",
                         max_length=100, required=True)
    ln = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}), label="Last name", max_length=100,
                         required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    cell = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '519-555-1212'}))
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )

    city = forms.CharField()
    province = forms.ChoiceField(choices=PROVINCES)
    postal_code = forms.CharField(label='Postal code', widget=forms.TextInput(attrs={'placeholder': 'N6H5L2'}))
    wants_email = forms.BooleanField(label='Send YAPCA-related emails to this parent\'s address')
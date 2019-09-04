from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.utils.translation import gettext_lazy as _

from ResumeForest.models import Profile, Bio, EmployerBio

MAX_UPLOAD_SIZE = 2500000


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("Invalid username/password")

        return cleaned_data


class RegistrationForm(forms.Form):
    CHOICES = (('employer', 'employer'), ('employee', 'employee'))
    username = forms.CharField(max_length=20,
                               widget=forms.TextInput(attrs={'class': "input100", 'placeholder': "username"}))
    password = forms.CharField(max_length=200,
                               label='Password',
                               widget=forms.PasswordInput(attrs={'class': "input100", 'placeholder': "password"}))
    confirm_password = forms.CharField(max_length=200,
                                       label='Confirm',
                                       widget=forms.PasswordInput(
                                           attrs={'class': "input100", 'placeholder': "confirm password"}))
    email = forms.CharField(max_length=50,
                            widget=forms.EmailInput(attrs={'class': "input100", 'placeholder': "email"}))
    first_name = forms.CharField(max_length=20,
                                 widget=forms.TextInput(attrs={'class': "input100", 'placeholder': "first name"}))
    last_name = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={'class': "input100", 'placeholder': "last name"}))

    user_type = forms.ChoiceField(choices=CHOICES,
                                  widget=forms.Select(attrs={'class': "input100"}))

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords did not match")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        return username


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerBio
        fields = ('er_position', 'company', 'education', 'er_location', 'email','message')
        labels = {
            'er_position': _('Position'),
            'er_location': _('Location')
        }
        widgets = {
            'er_position': forms.TextInput(attrs={'class': "input100"}),
            'company': forms.TextInput(attrs={'class': "input100"}),
            'education': forms.TextInput(attrs={'class': "input100"}),
            'er_location': forms.TextInput(attrs={'class': "input100"}),
            'email': forms.TextInput(attrs={'class': "input100"}),
            'message': forms.TextInput(attrs={'class':"input100"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


class SearchForm(forms.Form):
    Edu_Choices = (
        ('Empty', 'Choose the education level'),
        ('PhD', 'PhD'),
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('Other', 'Other')
    )

    education = forms.ChoiceField(choices=Edu_Choices, widget=forms.Select(attrs={'class': "input100"}))

    Pos_Choices = (
        ('Empty', 'Choose the job type'),
        ('Software Development Engineer', 'Software Development Engineer'),
        ('Machine Learning Engineer', 'Machine Learning Engineer'),
        ('Deep Learning Engineer', 'Deep Learning Engineer'),
        ('Hardware Engineer', 'Hardware Engineer'),
        ('Electrical Engineer', 'Electrical Engineer'),
        ('Big Data Engineer', 'Big Data Engineer'),
        ('Data Scientist', 'Data Scientist'),
        ('Business and Data Analyst', 'Business and Data Analyst'),
        ('Full Stack Engineer', 'Full Stack Engineer'),
        ('Other', 'Other')
    )
    position = forms.ChoiceField(choices=Pos_Choices, widget=forms.Select(attrs={'class': "input100"}))

    Loc_Choices = (
        ('Empty', 'Choose the location'),
        ('Alabama', 'Alabama'),
        ('Alaska', 'Alaska'),
        ('Arizona', 'Arizona'),
        ('Arkansas', 'Arkansas'),
        ('California', 'California'),
        ('Colorado', 'Colorado'),
        ('Connecticut', 'Connecticut'),
        ('Delaware', 'Delaware'),
        ('Florida', 'Florida'),
        ('Georgia', 'Georgia'),
        ('Hawaii', 'Hawaii'),
        ('Idaho', 'Idaho'),
        ('Illinois', 'Illinois'),
        ('Indiana', 'Indiana'),
        ('Iowa', 'Iowa'),
        ('Kansas', 'Kansas'),
        ('Kentucky', 'Kentucky'),
        ('Louisiana', 'Louisiana'),
        ('Maine', 'Maine'),
        ('Maryland', 'Maryland'),
        ('Massachusetts', 'Massachusetts'),
        ('Michigan', 'Michigan'),
        ('Minnesota', 'Minnesota'),
        ('Mississippi', 'Mississippi'),
        ('Missouri', 'Missouri'),
        ('Montana', 'Montana'),
        ('Nebraska', 'Nebraska'),
        ('Nevada', 'Nevada'),
        ('New Hampshire', 'New Hampshire'),
        ('New Jersey', 'New Jersey'),
        ('New Mexico', 'New Mexico'),
        ('New York', 'New York'),
        ('North Carolina', 'North Carolina'),
        ('North Dakota', 'North Dakota'),
        ('Ohio', 'Ohio'),
        ('Oklahoma', 'Oklahoma'),
        ('Oregon', 'Oregon'),
        ('Pennsylvania', 'Pennsylvania'),
        ('Rhode Island', 'Rhode Island'),
        ('South Carolina', 'South Carolina'),
        ('South Dakota', 'South Dakota'),
        ('Tennessee', 'Tennessee'),
        ('Texas', 'Texas'),
        ('Utah', 'Utah'),
        ('Vermont', 'Vermont'),
        ('Virginia', 'Virginia'),
        ('Washington', 'Washington'),
        ('West Virginia', 'West Virginia'),
        ('Wisconsin', 'Wisconsin'),
        ('Wyoming', 'Wyoming'),
        ('Other', 'Other')
    )

    location = forms.ChoiceField(choices=Loc_Choices, widget=forms.Select(attrs={'class': "input100"}))

    type_Choices = (
        ('Empty', 'Choose the job type'),
        ('Internship', 'Internship'),
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('On Campus', 'On Campus')
    )

    type = forms.ChoiceField(choices=type_Choices, widget=forms.Select(attrs={'class':"input100"}))

    contact_Choices = (
        ('Empty', 'Has contacted?'),
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Any', 'Any')

    )
    contact = forms.ChoiceField(choices=contact_Choices, widget=forms.Select(attrs={'class': "input100"}))

class EmailForm(forms.Form):
    message = forms.CharField(max_length=10000000,
                              widget=forms.TextInput(attrs={'class': "input100", 'placeholder': "last name"}))





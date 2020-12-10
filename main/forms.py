from django import forms
from django.forms import EmailInput, TextInput, ModelForm, IntegerField
from .models import UserRequest, Teacher
from.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['email', 'password']
        widgets = {
            "email": EmailInput(attrs={
                'placeholder': 'Your email'
            }),
            "password": TextInput(attrs={
                'placeholder': 'Your Password'
            }),
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'teacher_email', 'phone_number', 'teacher_password']
        widgets = {
            "teacher_name": TextInput(attrs={
                'placeholder': 'Your Name'
            }),
            "teacher_email": EmailInput(attrs={
                'placeholder': 'Your E-mail'
            }),
            "phone_number": TextInput(attrs={
                'placeholder': 'Your Phone'
            }),
            "teacher_password": TextInput(attrs={
                'placeholder': 'Your Password'
            }),
        }


class CreateForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput())
    user_phone = forms.CharField(widget=forms.TextInput())
    request_message = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = UserRequest
        fields = ['user_name', 'user_phone']


class OnlineOfferForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'contact_email', 'placeholder': 'Email'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'id': 'contact_subject', 'placeholder': 'Subject'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'id': 'contact_message', 'placeholder': 'Message', 'rows':'4'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'id':'contact_name', 'placeholder': 'Name'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'id':'contact_subject', 'placeholder': 'Phone'}), required=True)




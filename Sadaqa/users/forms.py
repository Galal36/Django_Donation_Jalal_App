from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    phone = PhoneNumberField(region="EG", label="Phone (Egyptian)")
    birthdate = forms.DateField(
        label="Birthdate", widget=forms.DateInput(attrs={"type": "date"})
    )
    pic = forms.ImageField(required=False, label="Profile Picture")
    country = forms.CharField(
        max_length=2, label="Country Code (e.g., EG)"
    )  # no trailing comma!

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        User = get_user_model()
        if User.objects.filter(phone=phone).exists():
            raise ValidationError("This phone number is already registered.")
        return phone

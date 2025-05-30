from allauth.account.adapter import DefaultAccountAdapter
from .forms import CustomSignupForm


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_signup_form_class(self, request):
        return CustomSignupForm

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        user.first_name = form.cleaned_data.get("first_name")
        user.last_name = form.cleaned_data.get("last_name")
        user.phone = form.cleaned_data.get("phone")
        user.birthdate = form.cleaned_data.get("birthdate")
        user.pic = form.cleaned_data.get("pic")
        user.country = form.cleaned_data.get("country")
        if commit:
            user.save()
        return user

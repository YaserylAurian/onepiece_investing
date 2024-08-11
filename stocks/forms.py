from django import forms
from .models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
    # username = forms.CharField(label='username', max_length=30)
    new_password = forms.CharField(label='password', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='password confirmation', widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', "Confirmation does not match password.")

    def save(self):
        super().save(commit=False)
        user = User.objects.create_user(
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('new_password')
        )
        return user
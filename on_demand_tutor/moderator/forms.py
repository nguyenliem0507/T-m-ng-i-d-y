from django import forms
from on_demand_tutor.models import User

class ModeratorRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'FullName', 'Phone', 'Email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

from django import forms


class loginform(forms.Form):

    email = forms.EmailField(required=True)
    password=forms.PasswordInput()



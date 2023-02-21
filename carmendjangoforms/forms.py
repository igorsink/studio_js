from django import forms


class userReg(forms.Form):
    name = forms.charField(max_length=100)
    email = forms.charField(max_length=100)
    password = forms.charField()


class userlogin(forms.Form):
    username = forms.charField(max_length=100)
    user_password = forms.charField()

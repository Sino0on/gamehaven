from game.models import Application
from django import forms


class ApplcationForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия Имя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Адрес электронной почты'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваше сообщение', 'rows': '3'}))

    class Meta:
        fields = ['fullname', 'email', 'phone_number', 'comment']
        model = Application

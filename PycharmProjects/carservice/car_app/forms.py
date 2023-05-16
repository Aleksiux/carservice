from django.contrib.auth.models import User

from .models import OrderComment, Profile
from django import forms


class OrdersCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ('content', 'order_list', 'commenter',)
        widgets = {'order': forms.HiddenInput(), 'commenter': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

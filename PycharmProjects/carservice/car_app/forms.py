from .models import OrderComment
from django import forms


class OrdersCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ('content', 'order', 'commenter',)
        widgets = {'order': forms.HiddenInput(), 'commenter': forms.HiddenInput()}
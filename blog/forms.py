from django import forms
from blog.models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'name',
            'comment',
        ]

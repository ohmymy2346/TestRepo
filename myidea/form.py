from django import forms

from .models import Article

class MyModelForm(forms.ModelForm):

    class Meta:

        model = Article
        fields = ('username','topic','description',)
from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["slug"].disabled = True
        # Or to set READONLY
        self.fields["slug"].widget.attrs["readonly"] = True
from django import forms
from .models import Article

# Create Newsletter Form
class NewsletterForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=30)
    email = forms.EmailField(label='Your Email Address')

# Create Article Post
class ArticleForm(forms.ModelForm):
    class meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags' = checkboxSelectMultiple(),
        }
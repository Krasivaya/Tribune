from django import forms

# Create Newsletter Form
class NewsletterForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=30)
    email = forms.EmailField(label='Your Email Address')
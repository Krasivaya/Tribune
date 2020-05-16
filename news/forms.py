from django import forms

# Create Newsletter Form
class NewsletterForm(forms.form):
    name = forms.CharField(label='Your Name', max_length=30)
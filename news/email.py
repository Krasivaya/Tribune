from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Welcome EMail
def welcome_mail(name, receiver):
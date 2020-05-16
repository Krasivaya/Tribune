from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Welcome EMail
def welcome_mail(name, receiver):
    subject = 'Welcome To The Tribune NewsLetter'
    sender = 'semwagacarine@gmail.com'
    

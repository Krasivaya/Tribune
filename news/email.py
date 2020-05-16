from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Welcome EMail
def welcome_mail(name, receiver):
    subject = 'Welcome To The Tribune NewsLetter'
    sender = 'semwagacarine@gmail.com'
        
    txt_content = render_to_string('email/welcome_mail.txt', {"name":name})
    html_content = render_to_string('email/welcome_mail.html', {"name":name})

    msg = EmailMultiAlternatives(subject, txt_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
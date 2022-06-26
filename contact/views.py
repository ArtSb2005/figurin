from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from contact.forms import ContactForm
from contact.models import Contact


class ContactCreate(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm
    success_message = 'Письмо отправлено'





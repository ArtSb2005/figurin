from django.forms import ModelForm, TextInput, EmailInput, Textarea

from contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'group', 'email', 'message']
        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Имя',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Фамилия',
                }
            ),
            'group': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Группа',
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Почта',
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Обращение',
                }
            ),
        }
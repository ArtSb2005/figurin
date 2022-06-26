import random
import requests
from django import template
import re

register = template.Library()


@register.simple_tag
def current_time(url, pk):
    try:
        name = pk
        try:
            file = open(f'media/{name}.jpg')
            return f'media/{name}.jpg'
        except IOError as e:
            fs = url[0].thumbnail_url
            img_data = requests.get(fs).content
            with open(f'media/{name}.jpg', 'wb') as handler:
                handler.write(img_data)
                return f'media/{name}.jpg'
    except:
        pass

@register.simple_tag
def caption_text(text):
    return text.split('\n')

@register.simple_tag
def user_pic(url, user):
    try:
        name = user
        file = open(f'media/{name}.jpg')
        return f'media/{name}.jpg'
    except:
        img_data = requests.get(url).content
        with open(f'media/{name}.jpg', 'wb') as handler:
            handler.write(img_data)
            return f'media/{name}.jpg'

@register.simple_tag
def price(text):
    try:
        return '₽'+re.search('✅.*?(\d+)', text).group(1)
    except:
        if ' '.join(re.findall(r'❌(.*?)❌', text)) == '':
            a = '₽'+' '.join(re.findall(r'🎠(.*?)🎠', text))
            if len(a) > 3:
                return '₽'+' '.join(re.findall(r'🎠(.*?)🎠', text))
            else:
                return ''
        else:
            a = '₽' + ' '.join(re.findall(r'❌(.*?)❌', text))
            if len(a) > 3:
                return '₽' + ' '.join(re.findall(r'❌(.*?)❌', text))
            else:
                return ''

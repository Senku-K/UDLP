from django.shortcuts import render
import os
from django.templatetags.static import static
from django.template.exceptions import TemplateDoesNotExist

def home(request):
    # Dictionary mapping user names to their HTML files
    users = {
        'Ritu Arora': 'ritu_arora.html',  # Just the filename without the profiles/ prefix
        'Arihant Chauhan': 'arihant_chauhan.html'
    }
    context = {
        'users': users,
        'bg_image': static('home/images/UDLP_bg.jpg')
    }
    return render(request, 'home/index.html', context)

def user_profile(request, filename):
    # Read the HTML file content
    template_path = f'home/profiles/{filename}'  # Add the profiles/ prefix here
    try:
        return render(request, template_path, {
            'bg_image': static('home/images/UDLP_bg.jpg')
        })
    except TemplateDoesNotExist:
        context = {
            'message': 'Profile not found',
            'bg_image': static('home/images/UDLP_bg.jpg')
        }
        return render(request, 'home/error.html', context)

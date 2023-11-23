from django.shortcuts import render, get_object_or_404
from .models import Blog, Media
# Create your views here.
def main(request):
    blog = Blog.objects.all()
    context = {
        "blog":blog
    }

    return render(request=request, template_name='main.html', context=context)

def details(request, id):
    media = get_object_or_404(Media, id= id)
    context = {
        'media':media
    }
    return render(request, 'detail.html', context)


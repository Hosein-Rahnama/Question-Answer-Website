from django.shortcuts import render
from blog import models as blog_models


def index(request):
    questions_list = blog_models.Question.objects.order_by('-published')
    context = {
        'questions_list': questions_list
    }
    template = 'blog/index.html'
    return render(request, template, context)
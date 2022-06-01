from django.shortcuts import render, get_object_or_404
from blog import models as blog_models


def index(request):
    questions_list = blog_models.Question.objects.order_by('-published')
    context = {
        'questions_list': questions_list
    }
    template = 'blog/index.html'
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(blog_models.Question, pk=question_id)
    answers = question.answer_set.order_by('-published').all()
    context = {
        'question': question,
        'answers': answers
    }
    template = 'blog/detail.html'
    return render(request, template, context)

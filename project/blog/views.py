from django.http import HttpResponse
from blog import models as blog_models

def index(request):
    questions_list = blog_models.Question.objects.order_by('-published')
    response = ''
    for question in questions_list:
        response += question.title + ', '
        for answer in question.answer_set.all():
            response += answer.author.username + ', '
    return HttpResponse(response)

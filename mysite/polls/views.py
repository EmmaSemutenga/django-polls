from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404

from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    #latest_question_list = get_list_or_404(Question, pub_date__year=2019), this uses filter() instead of get()
    #output = f", {[q.question_text for q in latest_question_list]}"
    #template = loader.get_template()
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', { 'question' : question })

# def results(request, question_id):
#     response = f"You are looking at the results of question {question_id}"
#     return HttpResponse(response)
#     return render(request, 'polls/index.html', context)

# def vote(request, question_id):
#     return HttpResponse(f"You are voting on question {question_id}")
#     return render(request, 'polls/index.html', context)
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = 'survey/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'survey/results.html'


def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)    
    try:
        selected_choice_id = int(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=selected_choice_id)
    
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponseRedirect(reverse('survey:index',))
        return HttpResponseRedirect(reverse('survey:ty',))

def ty(request):
    return render(request, 'survey/ty.html',)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Survey

class SurveyView(generic.ListView):
    template_name = 'survey/index.html'
    context_object_name = 'latest_survey_list'

    def get_queryset(self):
        return Survey.objects.order_by('-id')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = 'survey/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'survey/results.html'

def ty(request):
    return render(request, 'survey/ty.html')

def question_list(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    
    if request.method == 'POST':
        for question in survey.question_set.all():
            choice_id = request.POST.get(f'question{question.id}')
            if choice_id is not None:
                choice = question.choice_set.get(pk=choice_id)
                choice.votes += 1
                choice.save()
        return redirect('survey:thank_you')
    
    # return render(request, 'survey/question_list.html', {'survey': survey})
    return render(request, 'survey/questions.html', {'survey': survey})

def vote(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)

    if request.method == 'POST':
        for question in survey.question_set.all():
            choice_id = request.POST.get(f'question{question.id}')
            if choice_id is None: 
                return render(request, 'survey/detail.html', {
                    'survey': survey,
                    'error_message': "You didn't select a choice. Please select At least one choice. Thank You!",
                })
            else:
                choice = question.choice_set.get(pk=choice_id)
                choice.votes += 1
                choice.save()
                return redirect('survey:thank_you')
    
    return render(request, 'survey/survey_select.html', {'survey': survey})

# from django.contrib.auth.decorators import login_required
# from .forms import SurveyForm, QuestionFormSet, ChoiceFormSet

# @login_required
# def create_survey(request):
#     if request.method == 'POST':
#         survey_form = SurveyForm(request.POST)
#         question_formset = QuestionFormSet(request.POST, prefix='questions')
#         choice_formset = ChoiceFormSet(request.POST, prefix='choices')

#         if survey_form.is_valid() and question_formset.is_valid() and choice_formset.is_valid():
#             survey = survey_form.save(commit=False)
#             survey.creator = request.user
#             survey.save()

#             for form in question_formset:
#                 question = form.save(commit=False)
#                 question.survey = survey
#                 question.save()

#             for form in choice_formset:
#                 choice = form.save(commit=False)
#                 choice.question = question
#                 choice.save()

#             return redirect('survey/survey_select')

#     else:
#         survey_form = SurveyForm()
#         question_formset = QuestionFormSet(prefix='questions')
#         choice_formset = ChoiceFormSet(prefix='choices')

#     return render(request, 'survey/create_survey.html', {
#         'survey_form': survey_form,
#         'question_formset': question_formset,
#         'choice_formset': choice_formset
#     })


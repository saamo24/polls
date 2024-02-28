# from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.views import generic

# from .models import Question, Choice, Survey

# # Create your views here.

# class SurveyView(generic.ListView):
#     template_name = 'survey/index.html'
#     context_object_name = 'latest_survey_list'

#     def get_queryset(self):
#         return Survey.objects.order_by('-id')[:5]
    
# class QuestionView(generic.ListView):
#     template_name = 'surveu/index.thml'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         return Survey.objects.order_by('-id')[:5]


# class DetailView(generic.DeleteView):
#     model = Question
#     template_name = 'survey/detail.html'

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'survey/results.html'

# def vote(request, survey_id):

#     survey = get_object_or_404(Survey, pk=survey_id)    
#     try:
#         selected_choice_id = int(request.POST['choice'])
#         selected_choice = survey.choice_set.get(pk=selected_choice_id)
    
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'survey/detail.html', {
#             'survey': survey,
#             'error_message': "You didn't select a choice.",
#         })
    
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # return HttpResponseRedirect(reverse('survey:index',))
#         return HttpResponseRedirect(reverse('survey:ty',))

# def ty(request):
#     return render(request, 'survey/ty.html',)



# def question_list(request, survey_id):
#     survey = get_object_or_404(Survey, pk=survey_id)
    
#     if request.method == 'POST':
#         # Handle form submission
#         # This code assumes your form fields are named question1, question2, etc.
#         # Adjust the form field names based on your actual implementation
#         for question in survey.question_set.all():
#             choice_id = request.POST.get(f'question{question.id}')
#             if choice_id is not None:
#                 choice = question.choice_set.get(pk=choice_id)
#                 choice.votes += 1
#                 choice.save()
        
#         # Redirect to a thank you page or any other desired page
#         return redirect('survey:thank_you')
    
#     return render(request, 'survey/question_list.html', {'survey': survey})


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
    
    return render(request, 'survey/question_list.html', {'survey': survey})

def vote(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)

    if request.method == 'POST':
        for question in survey.question_set.all():
            choice_id = request.POST.get(f'question{question.id}')
            if choice_id is None: 
                return render(request, 'survey/detail.html', {
                    'survey': survey,
                    'error_message': "You didn't select a choice.",
                })
            else:
                choice = question.choice_set.get(pk=choice_id)
                choice.votes += 1
                choice.save()
                return redirect('survey:thank_you')
    
    return render(request, 'survey/survey_select.html', {'survey': survey})

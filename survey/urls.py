from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('', views.SurveyView.as_view(), name='index'),
    path('<int:survey_id>/', views.question_list, name='question_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:survey_id>/vote/', views.vote, name='vote'),
    path('thank-you/', views.ty, name='thank_you'),
    # path('create/', views.create_survey, name='create')
]

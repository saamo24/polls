# # from django.urls import path
# # from . import views


# # app_name = 'survey'
# # urlpatterns = [
# #     path('', view=views.SurveyView.as_view(), name='index'),
# #     path('<int:survey_id>/', views.question_list, name='question_list'),

# #     path('<int:pk>/', view=views.DetailView.as_view(), name='detail'),
# #     # path('<int:question_id>/vote', view=views.vote, name='vote'),
# #     path('thank-you', view=views.ty, name='ty')
# #     # path('<int:question_id>/results', view=views.results, name='results')

# # ]

# #erkrord
# from django.urls import path
# from . import views

# app_name = 'survey'
# urlpatterns = [
#     path('', views.SurveyView.as_view(), name='index'),
#     path('<int:survey_id>/', views.question_list, name='question_list'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:survey_id>/vote/', views.vote, name='vote'),  # Add this line
#     path('thank-you/', views.ty, name='ty'),
# ]

from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
    path('', views.SurveyView.as_view(), name='index'),
    path('<int:survey_id>/', views.question_list, name='question_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:survey_id>/vote/', views.vote, name='vote'),
    path('thank-you/', views.ty, name='thank_you')
]

from django.urls import path
from . import views


app_name = 'survey'
urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),
    path('<int:pk>/', view=views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote', view=views.vote, name='vote'),
    path('thank-you', view=views.ty, name='ty')
    # path('<int:question_id>/results', view=views.results, name='results')

]

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Feeling, FeelingGroup, Need, NeedGroup, Poem

class IndexView(generic.ListView):
    model = Feeling
    template_name = 'nvc/index.html'
    context_object_name = 'home'

            


class DetailView(generic.DetailView):
    model = Feeling
    template_name = 'nvc/detail.html'

    # def get_queryset(self):
    #     """
    #     Excludes any questions that aren't published yet.
    #     """
    #     return Question.objects.filter(pub_date__lte=timezone.now())


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

#     def get_queryset(self):
#         """
#         Excludes any results for questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())



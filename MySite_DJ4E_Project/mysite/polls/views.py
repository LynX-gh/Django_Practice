from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice

class owner(generic.TemplateView):
    template_name = "polls/owner.html"

class IndexView(generic.ListView):
    context_object_name = 'latest_question_list'
    template_name = "polls/index.html"

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.filter(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', { 'question':question, 'error_message':"You didn't select a choice!" })
    else:
        if selected_choice.exists():
            selected_choice.update(votes=F('votes') + 1)
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        else:
            return render(request, 'polls/detail.html', { 'question':question, 'error_message':"Invalid Choice!" })

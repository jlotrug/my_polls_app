from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.utils import timezone

#Generic Views
from django.views import generic

from .models import Question, Choice

#Generic Views
class IndexView(generic.ListView):
    template_name= 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #Return last five published questions
        return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

    #def get_contextt_object(Question):
    #    return Question.objects.get(pk=1)

    #breakpoint()

class DetailView(generic.DetailView):
    model = Question
    template_name= 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name= 'polls/results.html'





#Non Generic Views Except vote
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return render(request, 'polls/index.html', context)
#
#
#
#def detail(request, question_id):
#    #breakpoint()
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question, 'cool': 'cool beans'})
#
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    #breakpoint()
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #breakpoint()
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        return reverse('', args=(question_id,))

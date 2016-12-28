from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .models import Project, Image, About, Feedback
from django.forms import ModelForm
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class ProjectListView(ListView):

    model = Project
    template_name = 'projects.html'
    queryset = Project.objects.order_by('name')


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'comment', 'project']

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition', None)
        super(FeedbackForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['project'].widget = HiddenInput()


class ProjectDetailView(DetailView):

    model = Project
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm(initial={'project': self.object.pk}, hide_condition=True)
        context['feedback'] = Feedback.objects.filter(project=self.object.pk)
        return context


class FeedbackCreate(CreateView):

    model = Feedback
    form_class = FeedbackForm
    http_method_names = ['post']
    template_name = 'info.html'


def about(request):

    about = About.objects.get(pk=1)

    return render(request, 'about.html', {'about': about})


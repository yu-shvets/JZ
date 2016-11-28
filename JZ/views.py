from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project, Image, About

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class ProjectListView(ListView):

    model = Project
    template_name = 'projects.html'
    queryset = Project.objects.order_by('name')


class ProjectDetailView(DetailView):

    model = Project
    template_name = 'info.html'


def about(request):

    about = About.objects.get(pk=1)

    return render(request, 'about.html', {'about': about})


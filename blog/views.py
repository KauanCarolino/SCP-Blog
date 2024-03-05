from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
from blog.models import Publication

# Create your views here.

class BlogListView(ListView):
    template_name = "page/home.html"
    model = Publication

    def get_queryset(self, *args, **kwargs):
        return Publication.objects.filter(
            Q(is_published=True)
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogList"] = self.get_queryset()
        return context
    

class BlogDetailView(DetailView):
    template_name = "page/publication_detail.html"
    model = Publication

    queryset = Publication.objects.all()
    

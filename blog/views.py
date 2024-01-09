from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Publication

# Create your views here.

class BlogListView(ListView):
    template_name = "blog_page/pages/home.html"

    def get_queryset(self, *args, **kwargs):
        return Publication.objects.filter(
            is_published=True
        )
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["BlogList"] = self.get_queryset()
        return context
    
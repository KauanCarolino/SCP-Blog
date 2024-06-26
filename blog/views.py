from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView
from django_filters.views import FilterView
from blog.filters import PublicationFilterSet
from blog.models import Publication
from blog.utils import show_results_filter_set

# Create your views here.

class BlogListView(FilterView):
    template_name = "page/home.html"
    model = Publication
    filterset_class = PublicationFilterSet

    def get_queryset(self, *args, **kwargs):
        return self.model.objects.filter(is_published=True).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qr = self.request.GET.copy()

        context['filter_url'] = ('&' + qr.urlencode()) if len(qr) > 0 else ''
        context['show_results'] = show_results_filter_set(qr)
        context['filter'] = PublicationFilterSet(
            data=self.request.GET, queryset=self.get_queryset()
        )
        return context


class BlogDetailView(DetailView):
    template_name = "page/publication_detail.html"
    model = Publication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_detail_publication'] = True
        return context
    

class AboutlView(TemplateView):
    template_name = "page/about.html"
    model = Publication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ContactslView(TemplateView):
    template_name = "page/contacts.html"
    model = Publication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
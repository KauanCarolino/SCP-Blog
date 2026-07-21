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
    pk_url_kwarg = 'unique_id'

    def get_queryset(self):
        return super().get_queryset().select_related('author')

    THREAT_MAP = {
        'SAFE': {
            'label': 'Baixo',
            'color': 'bg-green-500',
            'width': '25%',
            'text_color': 'text-green-500',
        },
        'EUCLID': {
            'label': 'Médio',
            'color': 'bg-yellow-500',
            'width': '65%',
            'text_color': 'text-yellow-500',
        },
        'KETER': {
            'label': 'Alto',
            'color': 'bg-red-500',
            'width': '100%',
            'text_color': 'text-red-500',
        },
        'NOT_SPECIFIED': {
            'label': 'Desconhecido',
            'color': 'bg-gray-500',
            'width': '10%',
            'text_color': 'text-gray-500',
        },
    }

    CONTAINMENT_MAP = {
        Publication.StateContainment.CONTAINED: {
            'label': 'Contido',
            'badge': 'bg-green-900 text-green-400',
        },
        Publication.StateContainment.SAFE: {
            'label': 'Seguro',
            'badge': 'bg-blue-900 text-blue-400',
        },
        Publication.StateContainment.CRITICAL: {
            'label': 'Crítico',
            'badge': 'bg-red-900 text-red-400',
        },
    }
    CONTAINMENT_DEFAULT = {
        'label': 'Não informado',
        'badge': 'bg-gray-700 text-gray-400',
    }

    def get_threat_levels(self, obj: Publication) -> dict:
        return self.THREAT_MAP.get(obj.object_class, self.THREAT_MAP['NOT_SPECIFIED'])

    def get_containment_status(self, obj: Publication) -> dict:
        return self.CONTAINMENT_MAP.get(obj.state_containment, self.CONTAINMENT_DEFAULT)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        context['is_detail_publication'] = True
        context['threat_levels'] = self.get_threat_levels(obj)
        context['containment_status'] = self.get_containment_status(obj)
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
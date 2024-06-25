from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView
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


# class RecipeViewSearch(RecipeListviewBase):
#     template_name = 'recipes/pages/search.html'

#     def get_queryset(self, *args, **kwargs):
#         search_term = self.request.GET.get('q','')
#         qs = super().get_queryset(*args, **kwargs)
#         qs = qs.filter(
#             Q(
#             Q(title__icontains=search_term) |
#             Q(description__icontains=search_term),
#         ),
#         )
#         return qs   
    
#     def get_context_data(self, *args, **kwargs):
#         ctx = super().get_context_data(*args, **kwargs)
#         search_term = self.request.GET.get('q','')

#         ctx.update({
#         'page_title': f'Search for "{search_term}" |',
#         'search_term': search_term,
#         'additional_url_query': f'&q={search_term}',
#         })

#         return ctx

class BlogDetailView(DetailView):
    template_name = "page/publication_detail.html"
    model = Publication

    queryset = Publication.objects.all()
    

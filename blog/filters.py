import django_filters
from django.db.models import Q

from blog.models import Publication


class PublicationFilterSet(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label=('title'),
        method='filter_title_description')
    
    def filter_title_description(self, queryset, name, value):
        if value:
            queryset = queryset.filter(
                Q(title__icontains=value) |
                Q(resume__icontains=value)
            )
        return queryset
    
    class Meta:
        model = Publication
        fields = ['title']
import django_filters
from django.db.models import Q

from workshopApp.models import Login


class WorkerFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='Search',
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Login
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(mobile__icontains=value) |
            Q(email__icontains=value) |
            Q(address=value))
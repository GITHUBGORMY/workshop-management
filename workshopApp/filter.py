import django_filters

class workerfilter(django_filters.FilterSet):
    work_name =django_filters.CharFilter(field_name="name" ,label="", lookup_expr='icontains')
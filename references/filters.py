import django_filters
from .models import Companies

class CompaniesFilter(django_filters.FilterSet):
    class Meta:
        model = Companies
        fields = ['category', 'comapnyCountry']
        

        
    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
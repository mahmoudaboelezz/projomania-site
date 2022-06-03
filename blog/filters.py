import django_filters
from .models import Blogs

class ArticlesFilter(django_filters.FilterSet):
    class Meta:
        model = Blogs
        fields = ['category', 'author','title']
        

        
    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
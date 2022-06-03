from django.shortcuts import render
from .models import Blogs,Auto_Reply
from django.shortcuts import render ,get_object_or_404
from .filters import ArticlesFilter
from django.views.generic import ListView
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import Auto_Reply_Serializers
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

def Articles(request):
    articles = Blogs.objects.all()
    #filters
    filters = ArticlesFilter(request.GET,articles)
    filterdarticles = filters.qs
    paginator = Paginator(filterdarticles, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'filterdarticles': filterdarticles,'filters': filters,'page_obj':page_obj}
    if request.method == "POST":
        title = request.POST.get("search")
        articlesearch = Blogs.objects.filter(title__contains=title)
        search_result_count = articlesearch.count()
        if search_result_count <1:
            noresult = True
        else:
            noresult = False
        filterdarticles = articlesearch
        paginator = Paginator(filterdarticles, 2) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)       
        
        context = {'page_obj': page_obj,'filters': filters,'search_count':search_result_count,'noresult':noresult}
        

    
    return render(request, 'blogs/articles.html', context)

def Articledetail(request,slug):
    articlepage = get_object_or_404(Blogs, slug = slug)
    return render(request, 'blogs/articlepage.html', {'articlepage': articlepage , })

class viewsets_erros(viewsets.ModelViewSet):
    queryset = Auto_Reply.objects.all()
    serializer_class = Auto_Reply_Serializers
    
    
    # create a function to handle the post request
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
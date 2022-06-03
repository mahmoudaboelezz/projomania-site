from django.shortcuts import render

# Create your views here.
def apis_list(request):
    return render(request, 'build_apis/apis_list.html')
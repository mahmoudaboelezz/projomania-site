from django.shortcuts import render
from .models import Companies
from django.shortcuts import render ,get_object_or_404
from .filters import CompaniesFilter

# Create your views here.

def references(request):
    companies = Companies.objects.all()
    #filters
    filters = CompaniesFilter(request.GET,companies)
    companies = filters.qs
    
    return render(request, 'references/references.html', {'Companies': companies,'filters': filters})

def Companydetail(request,slug):
    company = get_object_or_404(Companies, slug = slug)
    return render(request, 'references/company.html', {'company': company , })

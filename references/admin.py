from django.contrib import admin
from .models import Companies
# Register your models here.


class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['companyName', 'comapnyCountry',
                    'category', 'companyLogo', 'companyUrl', 'comapyEmail']
    list_display_links = ['companyName']
    list_editable = ['comapnyCountry', 'category']
    search_fields = ['companyName']
    list_filter = ['category']


    
admin.site.register(Companies, CompaniesAdmin)
# Register your models here.

from django.contrib import admin
from django.db.models import fields
from .models import Blogs,Auto_Reply

# Register your models here.

class AutoReplyAdmin(admin.ModelAdmin):
    list_display = ['error']

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['title']
    # list_display_links = ['companyName']
    # list_editable = ['comapnyCountry', 'category']
    # search_fields = ['companyName']
    # list_filter = ['category']


    
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Auto_Reply, AutoReplyAdmin)
# Register your models here.

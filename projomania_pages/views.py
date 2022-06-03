from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render ,get_object_or_404
from django.contrib.auth.models import User
# Create your views here.




def homepage(request):
    return render(request, 'projomania_pages/index.html', {})


def aboutus(request):
    return render(request, 'projomania_pages/aboutus.html', {})


def ourteam(request):
    return render(request, 'projomania_pages/ourteam.html', {})



def odoo_database_migration(request):
    return render(request, 'projomania_pages/odoo_db_migration.html', {})


def odoo_code_upgrading(request):
    return render(request, 'projomania_pages/odoo_code_upgrading.html', {})


def linux_administration(request):
    return render(request, 'projomania_pages/linux_administration.html', {})


def odoo_apis(request):
    return render(request, 'projomania_pages/odoo_apis.html', {})


def install_odoo(request):
    return render(request, 'projomania_pages/install_odoo.html', {})


def debug_odoo(request):
    return render(request, 'projomania_pages/debug_odoo.html', {})


# def build_api_form(request):
#     return render(request, 'projomania_pages/build_api_form.html', {})


def odoo_module_development(request):
    return render(request, 'projomania_pages/odoo_module_development.html', {})


def partners(request):
    return render(request, 'projomania_pages/business_partners.html', {})



#create

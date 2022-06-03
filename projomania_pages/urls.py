from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.aboutus, name='aboutus'),
    path('team', views.ourteam, name='ourteam'),
    path('code_upgrade/', views.odoo_code_upgrading, name='odoo_code_upgrading'),
    path('odoo_db_migration/', views.odoo_database_migration, name='odoo_database_migration'),
    path('odoo_apis/', views.odoo_apis, name='odoo_apis'),
    path('install_odoo/', views.install_odoo, name='install_odoo'),
    path('debug_odoo/', views.debug_odoo, name='debug_odoo'),
    path('odoo_module_development/', views.odoo_module_development, name='odoo_module_development'),
    path('linux_administration/', views.linux_administration, name='linux_administration'),
    path('partners/', views.partners, name='ourpartners'),
    # path('references/', views.references, name='references'),
    # path('references/<slug:slug>/', views.Companydetail, name='companydetail'),

    
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
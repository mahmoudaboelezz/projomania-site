from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Companies(models.Model):

    x = [
        ('Database Migration', 'Database Migration'),
        ('Odoo Development', 'Odoo Development'),
        ('none','none'),
        ('---------','---------')
    ]
    y = [('usa','usa'),('belgim','belgim'),('Austria','Austria'),('none','none')]
    slug = models.SlugField(max_length=255,verbose_name="URL IN SITE", null=True, blank=True,)
    companyName = models.CharField(max_length=50, verbose_name="CompanyName")
    companyLogo = models.ImageField(
        upload_to='photos/%y/%m/%d', default="default.png")
    companyAdress = models.TextField(verbose_name="Adress",blank=True)
    companyUrl = models.CharField(max_length=200, verbose_name="URL",blank=True)
    comapyEmail = models.CharField(max_length=20, verbose_name="Email",blank=True)
    comapnyCountry = models.CharField(verbose_name="Country", max_length=50,choices=y,blank=True,default='none')
    
    class Meta:
        verbose_name = 'Companie'
        verbose_name_plural = 'Companies'
        
    def get_absolute_url(self):
        return reverse("companydetail",kwargs={"slug":self.slug})

    
    category = models.CharField(
        choices=x, max_length=50, null=True, blank=True,default='none',)

    def __str__(self):
        return self.companyName
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.companyName)
        super(Companies, self).save(*args, **kwargs)
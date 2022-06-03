from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.db.models import F

# Create your models here.
User = settings.AUTH_USER_MODEL

def image_upload_handler(instance,filename):
    #fpath = pathlib.Path(filename)

    path = f'addons/user_{instance.username}/{filename}'
    
class Auto_Reply(models.Model):
    error = models.TextField()
    solution = models.TextField()
    link = models.URLField()
    files = models.FileField(upload_to=image_upload_handler,null=True,blank=True)

    def __str__(self):
        return self.error
    class Meta:
        verbose_name = 'Error'
        verbose_name_plural = 'Errors'


class Blogs(models.Model):
    thumbnail = models.ImageField('thumbnails', default="default.png")
    slug = models.SlugField(max_length=255,verbose_name="URL IN SITE", null=True, blank=True,)
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE, blank=True)
    blog = models.TextField()
    added = models.DateTimeField(auto_now_add=True,verbose_name="Time added", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True,verbose_name="Last Updated", null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("articledetail",kwargs={"slug":self.slug})

    x = [('Database Migration', 'Database Migration'),
        ('Odoo Development', 'Odoo Development'),]
    category = models.CharField(
        choices=x, max_length=50, null=True, blank=True,default='none',)
    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'
        ordering = ['-added']
        # add - to desc and without to asc


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blogs, self).save(*args, **kwargs)
        

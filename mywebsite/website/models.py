from django.db import models
from datetime import date
from taggit.managers import TaggableManager 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Blog
class AddBlog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True, blank=True)
    pub_date = models.DateField(default=date.today)
    category = models.CharField(max_length=200, blank=True)
    sub_category = models.CharField(max_length=200, blank=True)

    tags = TaggableManager(blank=True)

    texteditor = RichTextUploadingField(blank=True, null=True)

    author= models.CharField(max_length=150, default="Codin India")
    
    def __str__(self):  
        return self.title
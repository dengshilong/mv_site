#coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from common import get_image_path
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    #cover = models.ImageField(u'图片', max_length=100L,upload_to=get_file_path)
    cover = models.ImageField(u'图片', max_length=100L, upload_to=get_image_path)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('movie.post', args=[str(self.id)])

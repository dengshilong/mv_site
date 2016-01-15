from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('movie.post', args=[str(self.id)])

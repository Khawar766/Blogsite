from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    blog_content = models.TextField()
    auther = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(blank=True,default=timezone.now)
    blog_views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250, unique_for_date='time_stamp',)
    thumbnail = models.ImageField(upload_to='blog',default="")
    
    def __str__(self):
        return 'Article '+self.title + ' by ' + self.auther
    def get_absolute_url(self):
        return reverse('blog:blogs',
                            args=[self.time_stamp.year,
                                    self.time_stamp.month,
                                    self.time_stamp.day, self.slug])
# making model for comment

class Blogcomment(models.Model):
    com_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blogpost,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    time_stamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment + ' by ' + str(self.user)
    
    
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE , null=False,blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to='images')

class comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE , null=False,blank=False)
    postc = models.ForeignKey(Post,on_delete=models.CASCADE)
    data=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
# Create your models here.

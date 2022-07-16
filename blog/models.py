from os import times_result
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.forms.widgets import Media
from django.utils import timezone


def user_directory(instance, filename):
    return 'user_{0}/{1}'.format(instance.uploader.username, filename)

class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True,upload_to=user_directory, null=True)
    url = models.CharField(max_length=500, blank=True, null= True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    # saved_post =

    def total_likes(self):
      return self.likes.count()

    def __str__(self):
      return self.title[:30] + ' | ' + str(self.uploader)

# class Save(models.Model):
#     post_object = models.ForeignKey(User, on_delete=models.CASCADE)
class Comments(models.Model):
  user_post = models.ForeignKey(Post, on_delete=CASCADE)
  user = models.ForeignKey(User, on_delete=CASCADE)
  comments = models.TextField(max_length=500, null=True, blank=True)
  created_on = models.DateTimeField(default=timezone.now)




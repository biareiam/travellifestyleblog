""" Libraries """
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    """  display the post categories"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """ Return to the home page """
        return reverse('home')


class Post (models.Model):
    """ Creating a post model """
    post_title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    category = models.CharField(max_length=255, default="Movies")
    likes = models.ManyToManyField(User, related_name="blog_posts")
    image = models.ImageField(null=False, blank=False, upload_to="images/",
                              default="placeholder")

    class Meta:
        """ Post sorted by date """
        ordering = ["-created_on"]

    def __str__(self):
        return self.post_title + ' | ' + str(self.author)

    def get_absolute_url(self):
        """ Return to the home page """
        return reverse('home')

    def total_likes(self):
        """ Count the likes """
        return self.likes.count()


class Comment(models.Model):
    """ Comment Model """
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_addded = models.DateField(auto_now_add=True)

    class Meta:
        """ Display the posts by date added """
        ordering = ["-date_addded"]

    def __str__(self):
        return '%s -%s' % (self.post.post_title, self.name)

from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.title
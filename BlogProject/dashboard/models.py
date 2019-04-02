from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    category_description=models.TextField()
    category_status=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.title
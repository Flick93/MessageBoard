from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):                                   #INHERITANCE
    title = models.CharField(max_length=128)                #composition
    subtitle = models.CharField(max_length=256)             #composition
    body = models.TextField()                               #composition
    created_on = models.DateTimeField(auto_now_add=True)    #composition

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
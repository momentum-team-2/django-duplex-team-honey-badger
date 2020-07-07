from django.db import models

# Create your models here.
class Snippet(models.Model):
    code = models.CharField(max_length=500)
    language = models.CharField(max_length=255)    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)   
    date_added = models.DateField(null=True, blank=True)
    # public/private
from django.db import models
from users.models import User

# Create your models here.
class Snippet(models.Model):
    code = models.TextField(max_length=500)
    language = models.CharField(max_length=255)    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)   
    date_added = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets', null=True)
    original_snippet = models.ForeignKey('self', on_delete=models.CASCADE, related_name='copied_snippets', null=True)
    
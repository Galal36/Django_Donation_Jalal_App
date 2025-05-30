from django.db import models
from users.models import Customuser

# Create your models here.
class Report (models.Model):
    customuser = models.OneToOneField( Customuser, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #we should do comment moderation

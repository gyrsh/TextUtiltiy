from django.db import models

# Create your models here.
class Posting(models.Model):
    username=models.CharField(max_length=50)
    email_id=models.CharField(max_length=100)

    def __str__(self):
        return self.username

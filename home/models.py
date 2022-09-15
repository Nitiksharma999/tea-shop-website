from django.db import models

# makemigrations = ceriate changes and store in a file
# migrate = apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name
    
    

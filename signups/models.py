from django.db import models

class SignUp(models.Model):
    name=models.CharField(max_length=30)
    

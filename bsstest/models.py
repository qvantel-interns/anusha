from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

class bsstest(models.Model):	
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)    
    mobilenumber=models.IntegerField(null=True, blank=True)

    def __unicode__(self):
    	return smart_unicode(self.name)



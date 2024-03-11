from django.db import models
from datetime import datetime

# Create your models here.
class AllServices(models.Model):
    slID = models.AutoField(primary_key=True)
    selectImage = models.ImageField( upload_to="AllServicesDBimgFolder")
    name = models.CharField(max_length=122)
    homepagecatagori = models.CharField(blank=True, null=True, max_length=50)
    Offer = models.IntegerField()
    silverPrice = models.IntegerField()
    silverLeads = models.CharField(max_length=40)
    silverDay = models.IntegerField()
    goldPrice = models.IntegerField()
    goldLeads = models.CharField(max_length=40)
    goldDay = models.IntegerField()
    diamondPrice = models.IntegerField()
    diamondLeads = models.CharField(max_length=40)
    diamondDay = models.IntegerField()
    desc = models.TextField()
    slag = models.SlugField(default="best")
    tags = models.CharField(max_length=200, blank=True, null=True,)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

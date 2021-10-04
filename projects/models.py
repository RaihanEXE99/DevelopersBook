from django.db import models
from django.contrib.auth.models import User

import random,string
import uuid

# Create your models here.
class Project(models.Model):
    class catagory(models.TextChoices):
        Web_Development = "Web_Development"
        App_Development = "App_Development"
        Game_Development = "Game_Development"
        Software_Development = "Software_development"
        Graphic_Design = "Graphic_Design"
        Bussiness_Management = "Bussiness_Management"
        Study_And_Assignment = "Study_And_Assignment"
        Script = "Script"
        Other = "Other"
    catagory = models.CharField(
        max_length=20,
        choices=catagory.choices,
        default=catagory.Web_Development
    )
    
    CreatedAt = models.DateTimeField(auto_now_add=True)
    projectName = models.CharField(max_length=40)
    Details = models.TextField(max_length=600)
    Requirements = models.TextField(max_length=500)
    github = models.URLField(default="https://github.com/404")
    discord = models.URLField(default="https://discord.com/404")
    facebook = models.URLField(default="https://www.facebook.com/error20%20404")
    Cusers = models.ManyToManyField(User, default=None)
    Cadmin = models.CharField(max_length=30, default=None)
    Finished = models.BooleanField(default=False)


    def __str__(self):
        return (self.projectName + "=>" + self.catagory)
    
    def onlyHalf(self):
        HDetails = str(self.Details)
        HDetails = HDetails[:90] + "....."
        return HDetails

    def onlyHalfR(self):
        HDetails = str(self.Requirements)
        HDetails = HDetails[:90] + "....."
        return HDetails
    
    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'Project'

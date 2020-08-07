from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class biox(models.Model):
    Cuser = models.OneToOneField(User,on_delete=models.CASCADE)
    userBio = models.TextField(max_length=250, default="Bio is Empty. Please update Profile")
    myFb = models.URLField(default="https://www.facebook.com/error20%20404")
    myGit = models.URLField(default="https://github.com/404")
    # myFb = models.URLField(default="https://www.facebook.com/error20%20404")
    # Cuser = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'biox'

class Notification(models.Model):
    projectName = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="projectName_set")
    reqUser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reqUser_set")
    message = models.TextField(max_length=500)
    toAdmin = models.CharField(max_length=100,default="Empty")

    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'Notification'
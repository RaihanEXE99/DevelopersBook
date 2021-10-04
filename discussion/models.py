from django.db import models
from django.contrib.auth.models import User
# from projects.models import Project


# Create your models here.
class SDiscussion(models.Model):
    title = models.CharField(max_length=70,default=None)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    Problem = models.TextField(max_length=2000)
    CreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    def onlyHalf(self):
        HDetails = str(self.Problem)
        HDetails = HDetails[:150] + "....."
        return HDetails

    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'SDiscussion'


class DComment(models.Model):
    Tdiscussion = models.ForeignKey(SDiscussion, on_delete=models.CASCADE)
    ComUser = models.ForeignKey(User, on_delete=models.CASCADE)
    myComment = models.TextField(max_length=2000)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Tdiscussion)
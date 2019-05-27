from django.db import models

# Create your models here.

class Action(models.Model):
    idAction = models.IntegerField()
    reason = models.CharField(max_length=30)
    duration = models.IntegerField()

class Intersection(models.Model):
    idIntersection = models.IntegerField()
    longitude = models.DecimalField(max_digits=20, decimal_places=10)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    intersectionName = models.CharField(max_length=300)

class Intervention(models.Model):
    idIntervention = models.IntegerField()
    actionIdx = models.ForeignKey(Action, on_delete=models.CASCADE)
    intersectionIdx = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    beginning = models.DateField(auto_now_add=True)
    ending = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=300)

class Vote(models.Model):
    idVote = models.IntegerField()
    intersectionIdx = models.ForeignKey(Intersection, on_delete=models.CASCADE)
    response = models.CharField(max_length=200)
    description = models.CharField(max_length=200)



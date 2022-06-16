from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class passenger(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    Address= models.CharField(blank=False, max_length=150)

    def __str__(self):
        return self.user.username


class line(models.Model):
    From =models.CharField(max_length=150, blank=False, null=False)
    to =models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.From+"_"+self.to



class train(models.Model):
    classes = (("first", "first"), ("second", "second"), ("third", "third"))

    line = models.ForeignKey(line, on_delete=models.CASCADE)
    departure=models.TimeField(blank=False)
    arrival = models.TimeField(blank=False)
    Class = models.CharField(max_length=150,choices=classes)


    def __str__(self):
        return self.line.From+"_"+self.line.to


class trip(models.Model):
    train=models.ForeignKey(train, on_delete=models.CASCADE)
    mount=models.IntegerField(blank=False)
    date= models.DateTimeField(blank=False)


    def __str__(self):
        return str(self.date)
from django.contrib.auth.models import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    about = models.TextField(max_length=250, blank=True, null=True)

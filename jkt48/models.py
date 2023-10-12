import os
from django.conf import settings
from django.db import models

# Create your models here.
class Member(models.Model):
    id_member = models.AutoField(primary_key=True)
    stage_name = models.CharField(max_length=20)
    gen = models.CharField(max_length=2)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    blood_type = models.CharField(max_length=2)
    horoskop = models.CharField(max_length=40)
    height = models.IntegerField()
    photo = models.ImageField(null=True, blank=True, default="{% static 'img/logo.png' %}", upload_to='media/mem-profile')
    is_capt = models.BooleanField(default=False)
    is_cent = models.BooleanField(default=False)
    is_trainee = models.BooleanField(default=False)

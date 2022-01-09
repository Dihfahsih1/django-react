from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  is_student = models.BooleanField()
  is_teacher = models.BooleanField()
  
  def __str__(self):
      return self.username
  
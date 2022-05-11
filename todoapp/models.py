from django.db import models
from userapp.models import Userapp

# Create your models here.

class Testapp(models.Model):

    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'

    PRIORITY_CHOICES = [
    (HIGH, 'High'),
    (MEDIUM, 'Medium'),
    (LOW, 'Low'),
    ]

    title = models.CharField(max_length=30)
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES, default=LOW)

    userapp = models.ForeignKey(Userapp, on_delete=models.CASCADE, null=True)

from django.db import models
from django.contrib.auth.models import User
import random

col = '#' + ''.join(random.sample('0123456789ABCDEF', k=6))

class UserColor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    col=models.TextField(default=col)



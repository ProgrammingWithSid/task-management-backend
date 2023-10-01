from django.db import models
import uuid
from users.models import UserAccount
# Create your models here.


class TaskApp(models.Model):
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    taskName = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    completedTill = models.DateTimeField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

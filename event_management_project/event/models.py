from django.db import models
from user.models import User

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length=200, null= False)
    description = models.TextField(null=False)
    event_date = models.DateTimeField(null=True )
    location = models.CharField(max_length=200,null=False)
    owner = models.OneToOneField(User, related_name='event_owner',on_delete= models.CASCADE)
    attendee = models.ManyToManyField(User, related_name='event_attendee', null=True, )

    def __str__(self):
        return self.title +" "+ str(self.event_date) +" "+ self.location +" "+ str(self.id)

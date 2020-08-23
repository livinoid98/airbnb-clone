from django.db import models
from core import models as core_models

class Review(core_models.TimeStampModel):

    review = models.TextField()
    accuracy = models.IntegerField()
    communications = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.room.host.username
    
    def rating_average(self):
        avg = (
            self.accuracy + self.communications + self.cleanliness + self.location + self.check_in + self.value
        )/6
        return round(avg, 2)
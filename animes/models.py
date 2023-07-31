from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Anime(models.Model):
    title = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    categoury = models.CharField(max_length=256)
    year = models.IntegerField()
    rate = models.IntegerField()
    # hotel_Main_Img = models.ImageField(upload_to='images/')
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
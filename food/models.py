from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTK99ZJCRNR_DJqeV7VfPMYcC9md4WtH3ItB8trBQfkbenGHxai-xmq7QqVxGWjG41mGwZBTCwcEYQ&usqp=CAU&ec=48665698")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
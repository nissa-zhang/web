from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self):
        return 'name[{0}] price[{1}]'.format(self.name, self.price)

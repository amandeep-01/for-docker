from django.db import models

# Create your models here.
class products(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    price=models.IntegerField()
    
    @property
    def getdiscount(self):
        return (0.8 *self.price)
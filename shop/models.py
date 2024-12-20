from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=300)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='items/')

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Product (models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=1000,default=10000)
    summary=models.TextField(default="its a nice product")
    featured=models.BooleanField(default=True)
    def absolute_url(self):
        return f"{self.id}/"
    

from django.db import models

class Device(models.Model):
    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    choices = (
        ('AVAILABLE', 'Item to be parchased'),
        ('SOLD', 'Item sold'),
        ('RESOURCING','Item resourcing in a few days')
    )
    status = models.CharField(max_length=10, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No issues")
    
    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type,self.price)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass

    
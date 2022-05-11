from django.db import models
from django.contrib import admin




class Goods(models.Model):
    name = models.CharField(max_length=200)
    date_come = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    quantity = models.SmallIntegerField()
    supplier = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        self.quantity + 1
        super(Goods, self).save(*args, **kwargs)


    class Meta:
        ordering = ('expiration_date',)



    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=200)
    time_open = models.TimeField()
    time_close = models.TimeField()
    quantity = models.IntegerField()
    address = models.CharField(max_length=200)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    SHOP_CHOICES = (
        ("p", "Product"),
        ("w", "Wear"),

    )
    view = models.CharField(max_length=1, choices=SHOP_CHOICES)

    def __str__(self):
        return self.name




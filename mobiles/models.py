from django.db import models

from django.db.models.deletion import DO_NOTHING



class Product_type(models.Model):
    product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name




class Product_details(models.Model):
    company_name = models.CharField(max_length=200, unique = True)
    price = models.FloatField(null=True, blank=True)
    photo = models.CharField(max_length=100, blank=True, default=None)
    ram = models.IntegerField(null=True, blank=True)
    rom = models.IntegerField(null=True, blank=True)
    expandable = models.IntegerField(null=True, blank=True)
    display = models.FloatField(null=True, blank=True)
    camera = models.CharField(max_length=100, blank=True)
    battery = models.IntegerField(null=True, blank=True)
    processor = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=200, blank=True)
    warranty = models.CharField(max_length=200, blank=True)
    star = models.FloatField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.IntegerField(null=True, blank=True)
    in_the_box = models.CharField(max_length=200, blank=True)
    product_type = models.ForeignKey(Product_type, blank=True, null=True, on_delete=DO_NOTHING)

    def __str__(self):
        return self.company_name



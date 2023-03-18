from django.db import models


class Category(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    status = models.SmallIntegerField(choices=[
        (1, 'Activo'),
        (2, 'Inactivo'),
    ], default=1)

    def __str__(self):
        return f'{self.code} - {self.name}'
    

class Product(models.Model):
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_products')
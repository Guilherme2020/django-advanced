from django.db.models.signals import post_save

from .stock.models import StockEntry

#receptor
def increment_stock(sender, instance, **kwargs):
    product = instance.product
    product.stock = product.stock + instance.amount
    product.save()

#post_save.connect(increment_stock,sender=StockEntry)

from django.db.models.signals import post_save

from stock.models import StockEntry

#receptor
def increment_stock(sender, instance,created, **kwargs):
    if created is True:
        product = instance.product
        product.stock = product.stock + instance.amount
        product.save()

def test_save(sender,instance,created,**kwargs):

    print(created)
def test_pre_save(sender,instance, **kwargs):
    print("Teste pre saved")
post_save.connect(increment_stock,sender=StockEntry)
post_save.connect(test_save,sender=StockEntry)
post_save.connect(test_pre_save,sender=StockEntry)

#pre_delete - antes de excluir
#post delete - depois de excluir

#m2m changed - quando a alteracao no relacionamento many to many
#request finished - quando tiver uma resposta http para ser enviada.


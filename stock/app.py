from django.apps import AppConfig


class StockConfig(AppConfig):
    name = 'stock'

    def ready(self):
        from stock import signals
        #from django.db.models.signals import post_save
        #from stock.signals import increment_stock
        #stock_entry = self.get_model('StockEntry')
        #post_save.connect(increment_stock, sender=stock_entry)
        #from django.db.models.signals import post_save
        #from stock.signals import increment_stock

        #
        #post_save.connect(increment_stock, sender=stock_entry)

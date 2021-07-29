from django.apps import AppConfig


class InventoryConfig(AppConfig):
    """
    Config App for Inventory application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'

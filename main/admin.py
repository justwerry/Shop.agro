from django.contrib import admin

from main.models import Shop, Goods

# admin.site.register(Shop)
# admin.site.register(Goods)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "view", 'quantity', 'time_open', 'time_close')
    list_filter = ['name', 'view']

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'expiration_date', 'date_come')
    list_filter = ['name', 'shop', 'expiration_date']




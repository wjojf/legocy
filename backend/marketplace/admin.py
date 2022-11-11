from django.contrib import admin
from .models import MarketItem, MarketItemImage


# Register your models here.
admin.site.register(MarketItemImage)
class MarketItemImageInline(admin.StackedInline):
    model = MarketItemImage
    extra = 1
    classes = ['extrapretty']


@admin.register(MarketItem)
class MarketItemAdmin(admin.ModelAdmin):
    inlines = [MarketItemImageInline]
    readonly_fields = ['created', 'last_modified']
    fieldsets = (
        ('Seller Info',{
            'fields': (
                'seller',
            )
        }),
        ('Listing info',{
            'fields': (
                'active',
                'created',
                'last_modified',
                'price',
                'currency',
            )
        }),
        ('Lego set',{
            'fields': (
                'lego_set',
            )
        })
    )
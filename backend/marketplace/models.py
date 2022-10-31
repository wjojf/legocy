from django.db import models
from core.models import LegoSet
from core.common_models import TimestampedModel, LikeDislike
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model
User = get_user_model()

from .utils import CURRENCY_CHOICES, market_item_image_filepath


# Create your models here.
class MarketItem(TimestampedModel):
    active = models.BooleanField(verbose_name='Listing is active', default=True)
    lego_set = models.ForeignKey(LegoSet, on_delete=models.CASCADE, verbose_name='LEGO set')
    ammount = models.PositiveIntegerField(null=False, default=1, verbose_name='Ammount of sets avaliable')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Seller')
    price = models.PositiveIntegerField(verbose_name='Selling price')
    currency = models.CharField(max_length=150, choices=CURRENCY_CHOICES)
    
    votes = GenericRelation(LikeDislike)

    class Meta:
        unique_together = ('seller', 'lego_set')


    @property
    def price_string(self):
        return f'{self.currency}{self.price}'


    def __str__(self):
        return f'{self.seller} {self.lego_set}'


class MarketItemImage(models.Model):
    market_item = models.ForeignKey(MarketItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=market_item_image_filepath, verbose_name='Item Image')


    def __str__(self):
        return f'{self.market_item} - {self.image.name}' 
    
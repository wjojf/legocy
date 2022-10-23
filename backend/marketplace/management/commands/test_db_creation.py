from django.contrib.auth.models import User
from django.core.management import BaseCommand

from core.models import LegoSeries, LegoSet
from marketplace.models import MarketItem


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.user = User.objects.create_user('test_user', 'test@test.com', 'asdf123!')
        self.user.save()
        self.lego_series = LegoSeries(name='New lego series')
        self.lego_series.save()
        self.lego_set = LegoSet(
            set_number=1,
            series=self.lego_series,
            title='New title',
            n_details=120
        )
        self.lego_set.save()
        self.market_item = MarketItem(
            active=True,
            lego_set=self.lego_set,
            seller=self.user,
            price=10,
            currency='USD'
        )
        self.market_item.save()
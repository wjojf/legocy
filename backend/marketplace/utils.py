CURRENCY_CHOICES = [
    ('USD', "$"),
    ('EUR', "€")
]


def market_item_image_filepath(instance, filename):
    return f'img/market_items/{instance.id}/'
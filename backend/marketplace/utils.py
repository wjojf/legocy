CURRENCY_CHOICES = [
    ('USD', "$"),
    ('EUR', "€")
]


def market_item_image_filepath(instance, filename):
    '''Returs string filepath for market item image'''
    return f'img/market_items/{instance.id}/'
from django.db import models


def lego_set_image_filepath(instance, filename):
    return 'img/legosets/{instance.id}/'

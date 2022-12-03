from django.db import models
from core.utils import lego_set_image_filepath, user_avatar_filepath 
from django.contrib.auth.models import AbstractBaseUser

from django.db.models.signals import post_delete
from .signals_utils import file_cleanup, images_cleanup


class LegocyUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(verbose_name='User avatar', upload_to=user_avatar_filepath)
    
    REQUIRED_FIELDS = ['email', 'password', 'avatar']
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return f'{self.username}'


class LegoSeries(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class LegoSet(models.Model):
    set_number = models.PositiveIntegerField(verbose_name='LEGO serial nubmer')
    series = models.ForeignKey(LegoSeries, on_delete=models.CASCADE, verbose_name='LEGO series')
    title = models.CharField(max_length=200, verbose_name='Set title')
    n_details = models.PositiveIntegerField(verbose_name='Number of details')

    class Meta:
        unique_together = ('set_number', 'series', 'title')

    @property
    def series_name(self):
        return self.series.name

    def __str__(self):
        return f'{self.set_number} - {self.title}'
post_delete.connect(
    images_cleanup,
    sender=LegoSet,
    dispatch_uid="LegoSet.images_cleanup"
)


class LegoSetImage(models.Model):

    lego_set = models.ForeignKey(LegoSet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=lego_set_image_filepath, verbose_name='Image File')


    def __str__(self):
        return f'{self.lego_set}: {self.image.name}'

post_delete.connect(
    file_cleanup,
    sender=LegoSetImage,
    dispatch_uid="LegoSetImage.file_cleanup"
)
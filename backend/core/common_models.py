from django.db import models
from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model
User = get_user_model()


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True
 
    def likes(self):
        # We take the queryset with records greater than 0
        return self.get_queryset().filter(vote__gt=0)
 
    def dislikes(self):
        # We take the queryset with records less than 0
        return self.get_queryset().filter(vote__lt=0)
 
    def sum_rating(self):
        # We take the total rating
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0


class TimestampedModel(models.Model):
    '''
    An abstract model that automatically provides `created`,
    `last_modified` fields.
    '''
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
 
class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
 
    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like')
    )
 
    vote = models.SmallIntegerField(verbose_name="Voice", choices=VOTES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Vote by')
 
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
 
    objects = LikeDislikeManager()
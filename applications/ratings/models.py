from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()

STAR = (
    (1, '1/5'),
    (2, '2/5'),
    (3, '3/5'),
    (4, '4/5'),
    (5, '5/5'),
)


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='ratings',
                             on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField(choices=STAR, help_text='max 5 stars')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id', 'star')

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Avg

from applications.likes.models import Like
from applications.ratings.models import Rating


# RATING = (
#     (1, '1/5'),
#     (2, '2/5'),
#     (3, '3/5'),
#     (4, '4/5'),
#     (5, '5/5'),
# )


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    likes = GenericRelation(Like)
    ratings = GenericRelation(Rating)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_rating(self):
        return Rating.objects.aggregate(Avg('star'))

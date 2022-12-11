from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg
from rest_framework import serializers

from applications.likes import services as likes_services
from applications.ratings import services as ratings_services

from applications.cinema.models import Movie
from applications.ratings.models import Rating


class MovieSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    is_reviewer = serializers.SerializerMethodField()
    total_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'description',
            'is_fan',
            'total_likes',
            'total_rating',
            'is_reviewer',
        )

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` фильм (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)

    def get_is_reviewer(self, obj) -> bool:
        """Проверяет, поставил ли `request.user` рейтинг фильму (`obj`).
        """
        user = self.context.get('request').user
        return ratings_services.is_reviewer(obj, user)

    @staticmethod
    def get_total_rating(obj):
        obj_type = ContentType.objects.get_for_model(obj)
        ratings = Rating.objects.filter(
            content_type=obj_type, object_id=obj.id).aggregate(Avg('star'))['star__avg']
        return ratings

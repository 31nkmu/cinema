from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import services
from .serializers import ReviewersSerializer


class GiveRatingMixin:

    @action(methods=['POST'], detail=True)
    def give_rating(self, request, pk=None):
        """Ставит рейтинг `obj`.
        """
        obj = self.get_object()
        star = request.data['star']
        if float(star) <= 5:
            services.add_rating(obj, request.user, star=star)
            return Response('Рейтинг успешно добавлен', status=status.HTTP_201_CREATED)
        return Response('Рейтинг должен быть не больше 5', status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=True)
    def del_rating(self, request, pk=None):
        """Удаляет рейтинг с `obj`.
        """
        obj = self.get_object()
        services.remove_rating(obj, request.user)
        return Response('Рейтинг успешно удален', status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def reviewers(self, request, pk=None):
        """Получает всех пользователей, которые поставили рейтинг `obj`.
        """
        obj = self.get_object()
        reviewers = services.get_reviewers(obj)
        serializer = ReviewersSerializer(reviewers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

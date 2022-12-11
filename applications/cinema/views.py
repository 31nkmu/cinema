from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from applications.cinema.models import Movie
from applications.cinema.serializers import MovieSerializer
from applications.likes.mixins import LikedMixin
from applications.ratings.mixins import GiveRatingMixin


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class MovieViewSet(LikedMixin, GiveRatingMixin, viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = LargeResultsSetPagination
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title']
    ordering_fields = ['id']

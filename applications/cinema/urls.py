from rest_framework.routers import DefaultRouter

from applications.cinema import views

# Создаем router и регистрируем ViewSet
router = DefaultRouter()
router.register('', views.MovieViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls

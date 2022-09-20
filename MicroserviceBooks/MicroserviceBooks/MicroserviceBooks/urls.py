from django.contrib import admin
from django.urls import path, include

from api import views
from rest_framework import routers

# Routers
routerEntity = routers.DefaultRouter()
routerV1 = routers.DefaultRouter()

# Router añade los endpoints a los viewsets
routerEntity.register('author', views.AuthorViewSet)
routerEntity.register('genre', views.GenreViewSet)
routerEntity.register('book', views.BookViewSet)
routerEntity.register('bookInstance', views.BookInstanceViewSet)

# routerV1.register('login', views.LoginViewSet)

urlpatterns = [
  path('', views.index.as_view(), name='index'),
  path('health/', views.health.as_view(), name='health'),
  path('api/v1/login/', views.login.as_view(), name='login'),
  # path('api/v1/', include(routerV1.urls)),
  path('api/entity/', include(routerEntity.urls)),
  path('admin/', admin.site.urls)
]

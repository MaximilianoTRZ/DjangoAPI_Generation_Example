from django.contrib import admin
from django.urls import path, include
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.routes.entityRoutes.entityRoutes import routerEntities
from api.routes.v1Routes.v1Routes import routerV1
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import IsAuthenticated


class index(APIView):

    def get(self, request, format=None):
      return Response('',status=status.HTTP_200_OK)

class health(APIView):
    def get(self, request, format=None):
      return Response('ok',status=status.HTTP_200_OK)

urlpatterns = [
  path('', index.as_view(), name='index'),
  path('health/', health.as_view(), name='health'),
  path('api/entity/', include(routerEntities.urls)),
  path('api/v1/', include(routerV1.urls)),
  path('admin/', admin.site.urls)
]
